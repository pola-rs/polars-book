# Temporal groupby with `groupby_dynamic`

We can calculate temporal statistics using `groupby_dynamic` to group rows into days/months/years etc.

## Annual average example
The following simple example captures the mean features of using `groupby_dynamic`. We take a time series of Apple stock prices and want to compute the annual average of the opening price.

We first load the data from CSV:

```python
df = pl.read_csv("apple_stock.csv", parse_dates=True)
```
```
┌────────────┬───────┐
│ Date       ┆ Open  │
│ ---        ┆ ---   │
│ date       ┆ f64   │
╞════════════╪═══════╡
│ 1980-12-12 ┆ 28.75 │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 1980-12-15 ┆ 27.38 │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ ...        ┆ ...   │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2014-07-07 ┆ 94.14 │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌┤
│ 2014-07-08 ┆ 96.27 │
└────────────┴───────┘
```
> Note that the dates are sorted in ascending order - if they are not sorted in this manner the output will not be correct!

To get the annual average we tell `groupby_dynamic` that we want to:
- group by the `Date` column every year 
- take the mean values of the `Open` column for each year:
```python
df.groupby_dynamic("Date",every='1y').agg(pl.col("Open").mean())
```
The output is then:
```
┌────────────┬────────────┐
│ Date       ┆ Open       │
│ ---        ┆ ---        │
│ date       ┆ f64        │
╞════════════╪════════════╡
│ 1980-01-01 ┆ 30.481538  │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┤
│ 1981-01-01 ┆ 24.386349  │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┤
│ ...        ┆ ...        │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┤
│ 2013-01-01 ┆ 473.128135 │
├╌╌╌╌╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌╌╌╌╌┤
│ 2014-01-01 ┆ 477.553256 │
└────────────┴────────────┘
```
### Paramters for `groupby_dynamic`
The value for `every` sets how often the groups start. The values are not fixed - for example we could take:
- the average over 2 year intervals by replacing `1y` with `2y`
- the average over 18 month periods by replacing `1y` with `1y6mo`

We can also use the `period` parameter to set how long the time period for each group is. For example, if we set the `every` parameter to be `1y` and the `period` parameter to be `2y` then we would get groups at one year intervals where each groups spanned two years.

See [the API pages](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.DataFrame.groupby_dynamic.html) for the full range of time periods.

The `truncate` is a Boolean parameter that affects the datetime value for each group in the output. In the example above the first data point is on 12th December 1980. If `truncate = True` (the default) then the date for the first year in the annual average is 1st January 1980. However, if `truncate = False` then the date for the first year in the annual average is the date of the first data point on 12th December 1980.


In the snippet below we create a `date range` with every **day** (`"1d"`) in 2021 and turn this into a `DataFrame`.

Then we we create dynamic windows that starts every **month** (`"1mo"`) and has a window length of `1` month. Dynamic windows
don't have a size thats fixed by the number of rows in a `DataFrame`, instead they are fixed by a temporal unit. This can
be a day (`"1d"`), `3` weeks (`"3w"`) or `5` nanoseconds (`"5ns"`) ... you get the idea.

The values that match these dynamic windows are then assigned to that group and can be aggregated with the powerful expression API.

Below we show an example where we use **groupby_dynamic** to compute:

- the number of days until the end of the month
- the number of days in a month

```python
{{#include ../examples/time_series/days_month.py:4:}}
print(out)
```

```text
{{#include ../outputs/time_series/days_month.txt}}
```

A dynamic window is defined by a:

- **every**: indicates the interval of the window
- **period**: indicates the duration of the window
- **offset**: can be used to offset the start of the windows

Because _**every**_ does not have to be equal to _**period**_, we can create many groups in a very flexible way. They may overlap
or leave boundaries between them.

Let's see how the windows for some parameter combinations would look. Let's start out boring. 🥱

>

- every: 1 day -> `"1d"`
- period: 1 day -> `"1d"`

```text
this creates adjacent windows of the same size
|--|
   |--|
      |--|
```

>

- every: 1 day -> `"1d"`
- period: 2 days -> `"2d"`

```text
these windows have an overlap of 1 day
|----|
   |----|
      |----|
```

>

- every: 2 days -> `"2d"`
- period: 1 day -> `"1d"`

```text
this would leave gaps between the windows
data points that in these gaps will not be a member of any group
|--|
       |--|
              |--|
```

## Rolling GroupBy

The rolling groupby is another entrance to the `groupby` context. But different from the `groupby_dynamic` the windows are
not fixed by a parameter `every` and `period`. In a rolling groupby the windows are not fixed at all! They are determined
by the values in the `index_column`.

So imagine having a time column with the values `{2021-01-01, 20210-01-05}` and a `period="5d"` this would create the following
windows:

```text

2021-01-01   2021-01-06
    |----------|

       2021-01-05   2021-01-10
             |----------|
```

Because the windows of a rolling groupby are always determined by the values in the `DataFrame` column, the number of
groups is always equal to the original `DataFrame`.

## Combining Groupby and Dynamic / Rolling

Rolling and dynamic groupby's can be combined with normal groupby operations.

Below is an example with a dynamic groupby.

```python
{{#include ../examples/time_series/dynamic_ds.py:0:}}
print(out)
```

```text
{{#include ../outputs/time_series/dyn_df.txt}}
```

```python
{{#include ../examples/time_series/dynamic_groupby.py:4:}}
print(out)
```

```text
{{#include ../outputs/time_series/dyn_gb.txt}}
```

## Upsample

> This content is under construction.
