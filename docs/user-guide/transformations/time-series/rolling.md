# Grouping

## Grouping by fixed windows

We can calculate temporal statistics using `groupby_dynamic` to group rows into days/months/years etc.

### Annual average example

In following simple example we calculate the annual average closing price of Apple stock prices. We first load the data from CSV:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/rolling.py:df"
    ```

```text
shape: (100, 2)
┌────────────┬────────┐
│ Date       ┆ Close  │
│ ---        ┆ ---    │
│ date       ┆ f64    │
╞════════════╪════════╡
│ 1981-02-23 ┆ 24.62  │
│ 1981-05-06 ┆ 27.38  │
│ 1981-05-18 ┆ 28.0   │
│ 1981-09-25 ┆ 14.25  │
│ …          ┆ …      │
│ 2012-12-04 ┆ 575.85 │
│ 2013-07-05 ┆ 417.42 │
│ 2013-11-07 ┆ 512.49 │
│ 2014-02-25 ┆ 522.06 │
└────────────┴────────┘
```

!!! info 
    The dates are sorted in ascending order - if they are not sorted in this way the `groupby_dynamic` output will not be correct!

To get the annual average closing price we tell `groupby_dynamic` that we want to:

- group by the `Date` column on an annual (`1y`) basis
- take the mean values of the `Close` column for each year:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/rolling.py:groupby"
    ```

The annual average closing price is then:

```text
shape: (34, 2)
┌────────────┬───────────┐
│ Date       ┆ Close     │
│ ---        ┆ ---       │
│ date       ┆ f64       │
╞════════════╪═══════════╡
│ 1981-01-01 ┆ 23.5625   │
│ 1982-01-01 ┆ 11.0      │
│ 1983-01-01 ┆ 30.543333 │
│ 1984-01-01 ┆ 27.583333 │
│ …          ┆ …         │
│ 2011-01-01 ┆ 368.225   │
│ 2012-01-01 ┆ 560.965   │
│ 2013-01-01 ┆ 464.955   │
│ 2014-01-01 ┆ 522.06    │
└────────────┴───────────┘
```

### Parameters for `groupby_dynamic`

A dynamic window is defined by a:

- **every**: indicates the interval of the window
- **period**: indicates the duration of the window
- **offset**: can be used to offset the start of the windows

The value for `every` sets how often the groups start. The time period values are flexible - for example we could take:

- the average over 2 year intervals by replacing `1y` with `2y`
- the average over 18 month periods by replacing `1y` with `1y6mo`

We can also use the `period` parameter to set how long the time period for each group is. For example, if we set the `every` parameter to be `1y` and the `period` parameter to be `2y` then we would get groups at one year intervals where each groups spanned two years.

If the `period` parameter is not specified then it is set equal to the `every` parameter so that if the `every` parameter is set to be `1y` then each group spans `1y` as well.

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

#### `truncate`

The `truncate` parameter is a Boolean variable that determines what datetime value is associated with each group in the output. In the example above the first data point is on 23rd February 1981. If `truncate = True` (the default) then the date for the first year in the annual average is 1st January 1981. However, if `truncate = False` then the date for the first year in the annual average is the date of the first data point on 23rd February 1981.

### Using expressions in `groupby_dynamic`

We aren't restricted to using simple aggregations like `mean` in a groupby operation - we can use the full range of expressions available in Polars.

In the snippet below we create a `date range` with every **day** (`"1d"`) in 2021 and turn this into a `DataFrame`.

Then in the `groupby_dynamic` we create dynamic windows that start every **month** (`"1mo"`) and have a window length of `1` month. The values that match these dynamic windows are then assigned to that group and can be aggregated with the powerful expression API.

Below we show an example where we use **groupby_dynamic** to compute:

- the number of days until the end of the month
- the number of days in a month

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/rolling.py:groupbydyn"
    ```

```text
shape: (36, 3)
┌─────────────────────┬─────────┬───────────────┐
│ time                ┆ day/eom ┆ days_in_month │
│ ---                 ┆ ---     ┆ ---           │
│ datetime[μs]        ┆ u32     ┆ i64           │
╞═════════════════════╪═════════╪═══════════════╡
│ 2021-01-01 00:00:00 ┆ 30      ┆ 31            │
│ 2021-01-01 00:00:00 ┆ 29      ┆ 31            │
│ 2021-01-01 00:00:00 ┆ 28      ┆ 31            │
│ 2021-02-01 00:00:00 ┆ 27      ┆ 28            │
│ …                   ┆ …       ┆ …             │
│ 2021-11-01 00:00:00 ┆ 27      ┆ 30            │
│ 2021-12-01 00:00:00 ┆ 30      ┆ 31            │
│ 2021-12-01 00:00:00 ┆ 29      ┆ 31            │
│ 2021-12-01 00:00:00 ┆ 28      ┆ 31            │
└─────────────────────┴─────────┴───────────────┘
```

## Grouping by rolling windows

The rolling groupby, `groupby_rolling`, is another entrance to the `groupby` context. But different from the `groupby_dynamic` the windows are
not fixed by a parameter `every` and `period`. In a rolling groupby the windows are not fixed at all! They are determined
by the values in the `index_column`.

So imagine having a time column with the values `{2021-01-06, 20210-01-10}` and a `period="5d"` this would create the following
windows:

```text

2021-01-01   2021-01-06
    |----------|

       2021-01-05   2021-01-10
             |----------|
```

Because the windows of a rolling groupby are always determined by the values in the `DataFrame` column, the number of
groups is always equal to the original `DataFrame`.

## Combining Groupby's

Rolling and dynamic groupby's can be combined with normal groupby operations.

Below is an example with a dynamic groupby.

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/rolling.py:groupbyroll"
    ```
    
```text
shape: (7, 2)
┌─────────────────────┬────────┐
│ time                ┆ groups │
│ ---                 ┆ ---    │
│ datetime[μs]        ┆ str    │
╞═════════════════════╪════════╡
│ 2021-12-16 00:00:00 ┆ a      │
│ 2021-12-16 00:30:00 ┆ a      │
│ 2021-12-16 01:00:00 ┆ a      │
│ 2021-12-16 01:30:00 ┆ b      │
│ 2021-12-16 02:00:00 ┆ b      │
│ 2021-12-16 02:30:00 ┆ a      │
│ 2021-12-16 03:00:00 ┆ a      │
└─────────────────────┴────────┘
```

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/rolling.py:groupbydyn2"
    ```

```text
shape: (7, 5)
┌────────┬─────────────────────┬─────────────────────┬─────────────────────┬───────┐
│ groups ┆ _lower_boundary     ┆ _upper_boundary     ┆ time                ┆ count │
│ ---    ┆ ---                 ┆ ---                 ┆ ---                 ┆ ---   │
│ str    ┆ datetime[μs]        ┆ datetime[μs]        ┆ datetime[μs]        ┆ u32   │
╞════════╪═════════════════════╪═════════════════════╪═════════════════════╪═══════╡
│ a      ┆ 2021-12-15 23:00:00 ┆ 2021-12-16 00:00:00 ┆ 2021-12-15 23:00:00 ┆ 1     │
│ a      ┆ 2021-12-16 00:00:00 ┆ 2021-12-16 01:00:00 ┆ 2021-12-16 00:00:00 ┆ 3     │
│ a      ┆ 2021-12-16 01:00:00 ┆ 2021-12-16 02:00:00 ┆ 2021-12-16 01:00:00 ┆ 1     │
│ a      ┆ 2021-12-16 02:00:00 ┆ 2021-12-16 03:00:00 ┆ 2021-12-16 02:00:00 ┆ 2     │
│ a      ┆ 2021-12-16 03:00:00 ┆ 2021-12-16 04:00:00 ┆ 2021-12-16 03:00:00 ┆ 1     │
│ b      ┆ 2021-12-16 01:00:00 ┆ 2021-12-16 02:00:00 ┆ 2021-12-16 01:00:00 ┆ 2     │
│ b      ┆ 2021-12-16 02:00:00 ┆ 2021-12-16 03:00:00 ┆ 2021-12-16 02:00:00 ┆ 1     │
└────────┴─────────────────────┴─────────────────────┴─────────────────────┴───────┘
```