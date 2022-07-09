# Resampling

We can resample by either:

- upsampling (moving data to a higher frequency)
- downsampling (moving data to a lower frequency)
- combinations of these e.g. first upsample and then downsample

## Downsampling to a lower frequency

`Polars` views downsampling as a special case of the **groupby** operation and you can do this with `groupby_dynamic` and `groupby_rolling` - [see the temporal groupby page for examples](temporal_groupby.md).

## Upsampling to a higher frequency

Let's go through an example where we generate data at 30 minute intervals:

```python
{{#include ../../examples/time_series/resampling_example.py:0:10}}
print(df)
```

```text
{{#include ../../outputs/time_series/resample_example_df.txt}}
```

Upsampling can be done by defining the new sampling interval. By upsampling we are adding in extra rows where we do not have data. As such upsampling by itself gives a DataFrame with nulls. These nulls can then be filled with a fill strategy or interpolation.

### Upsampling strategies

In this example we upsample from the original 30 minutes to 15 minutes and then use a `forward` strategy to replace the nulls with the previous non-null value:

```python
{{#include ../../examples/time_series/resampling_example.py:12:12}}
print(out1)
```

```text
{{#include ../../outputs/time_series/resample_upsample_output.txt}}
```

In this example we instead fill the nulls by linear interpolation:

```python
{{#include ../../examples/time_series/resampling_example.py:14:}}
print(out2)
```

```text
{{#include ../../outputs/time_series/resample_upsample_interpolation.txt}}
```
