# Time Series

For time-series resampling polars offers a powerful API to resample data. I think everybody gives pandas credit for
their resampling functionality via `df.resample`.

Polars make the distinction between

- upsampling
- downsampling

## Upsampling

An upsample operation is actually nothing more than left joining a date range with your dataset and filling the blanks.
Polars provides wrapper methods for this operations and we will show an example later.

## Downsampling

Downsampling is the interesting part. How do you deal with date intervals, window durations, aggregations etc.

Polars sees downsampling as special case of the **groupby** operation and therefore has two extra entrances in the
expression API with the `groupby context`:

- [groupby_dynamic](POLARS_PY_REF_GUIDE/api/polars.DataFrame.groupby_dynamic.html)
- [groupby_rolling](POLARS_PY_REF_GUIDE/api/polars.DataFrame.groupby_rolling.html)

Calling any of those functions will give you complete access to the expression API and performance!

Let's go through some examples and see what that means.

## Groupby Dynamic

In the snippet below we create a `date range` with every **day** (`"1d"`) in 2021 and turn this into a `DataFrame`.

Then we we create dynamic windows that starts every **month** (`"1mo"`) and has a window length of 1 month. Dynamic windows
don't have a size thats fixed by the number of rows in a `DataFrame`, instead they are fixed by a temporal unit. This can
be a day (`"1d"`), 3 weeks (`"3w"`), 5 nanoseconds (`"5ns"`) you get the idea.

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

- **every** indicates the interval of the window
- **period** indicates the duration of the window
- **offset** can be used to offset the start of the windows

Because **every** does not have to be equal to **period** we can create many groups in a very flexible way. They may overlap
or leave boundaries between them.

Let's see how the windows for some parameter combinations would look. Let's start boring:

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

## Rolling groupby

The rolling groupby is another entrance to the `groupby context`. But different from the `groupby_dynamic` the windows are
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

## Combining Groupby + Dynamic / Rolling

Rolling and dynamic groupby's can be combined with normal groupby operations.

Below we show an example with a dynamic groupby.

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

> in redaction
