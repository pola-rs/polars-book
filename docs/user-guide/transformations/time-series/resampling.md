# Resampling

We can resample by either:

- upsampling (moving data to a higher frequency)
- downsampling (moving data to a lower frequency)
- combinations of these e.g. first upsample and then downsample

## Downsampling to a lower frequency

`Polars` views downsampling as a special case of the **groupby** operation and you can do this with `groupby_dynamic` and `groupby_rolling` - [see the temporal groupby page for examples](rolling.md).

## Upsampling to a higher frequency

Let's go through an example where we generate data at 30 minute intervals:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/resampling.py:df"
    ```

```text
shape: (7, 3)
┌─────────────────────┬────────┬────────┐
│ time                ┆ groups ┆ values │
│ ---                 ┆ ---    ┆ ---    │
│ datetime[μs]        ┆ str    ┆ f64    │
╞═════════════════════╪════════╪════════╡
│ 2021-12-16 00:00:00 ┆ a      ┆ 1.0    │
│ 2021-12-16 00:30:00 ┆ a      ┆ 2.0    │
│ 2021-12-16 01:00:00 ┆ a      ┆ 3.0    │
│ 2021-12-16 01:30:00 ┆ b      ┆ 4.0    │
│ 2021-12-16 02:00:00 ┆ b      ┆ 5.0    │
│ 2021-12-16 02:30:00 ┆ a      ┆ 6.0    │
│ 2021-12-16 03:00:00 ┆ a      ┆ 7.0    │
└─────────────────────┴────────┴────────┘
```

Upsampling can be done by defining the new sampling interval. By upsampling we are adding in extra rows where we do not have data. As such upsampling by itself gives a DataFrame with nulls. These nulls can then be filled with a fill strategy or interpolation.

### Upsampling strategies

In this example we upsample from the original 30 minutes to 15 minutes and then use a `forward` strategy to replace the nulls with the previous non-null value:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/resampling.py:upsample"
    ```

```text
shape: (13, 3)
┌─────────────────────┬────────┬────────┐
│ time                ┆ groups ┆ values │
│ ---                 ┆ ---    ┆ ---    │
│ datetime[μs]        ┆ str    ┆ f64    │
╞═════════════════════╪════════╪════════╡
│ 2021-12-16 00:00:00 ┆ a      ┆ 1.0    │
│ 2021-12-16 00:15:00 ┆ a      ┆ 1.0    │
│ 2021-12-16 00:30:00 ┆ a      ┆ 2.0    │
│ 2021-12-16 00:45:00 ┆ a      ┆ 2.0    │
│ …                   ┆ …      ┆ …      │
│ 2021-12-16 02:15:00 ┆ b      ┆ 5.0    │
│ 2021-12-16 02:30:00 ┆ a      ┆ 6.0    │
│ 2021-12-16 02:45:00 ┆ a      ┆ 6.0    │
│ 2021-12-16 03:00:00 ┆ a      ┆ 7.0    │
└─────────────────────┴────────┴────────┘
```

In this example we instead fill the nulls by linear interpolation:

=== ":fontawesome-brands-python: Python"
    ``` python
    --8<-- "user-guide/python/transformations/time-series/resampling.py:upsample2"
    ```

```text
shape: (13, 3)
┌─────────────────────┬────────┬────────┐
│ time                ┆ groups ┆ values │
│ ---                 ┆ ---    ┆ ---    │
│ datetime[μs]        ┆ str    ┆ f64    │
╞═════════════════════╪════════╪════════╡
│ 2021-12-16 00:00:00 ┆ a      ┆ 1.0    │
│ 2021-12-16 00:15:00 ┆ a      ┆ 1.5    │
│ 2021-12-16 00:30:00 ┆ a      ┆ 2.0    │
│ 2021-12-16 00:45:00 ┆ a      ┆ 2.5    │
│ …                   ┆ …      ┆ …      │
│ 2021-12-16 02:15:00 ┆ b      ┆ 5.5    │
│ 2021-12-16 02:30:00 ┆ a      ┆ 6.0    │
│ 2021-12-16 02:45:00 ┆ a      ┆ 6.5    │
│ 2021-12-16 03:00:00 ┆ a      ┆ 7.0    │
└─────────────────────┴────────┴────────┘
```