# Interact with AWS

> The Interact with AWS page is under construction.

To read from or write to an AWS bucket, additional dependencies are needed:

```shell
$ pip install s3fs
```

In the next few snippets we'll demonstrate interacting with a `Parquet` file
located on an AWS bucket.

## Read

Load a `.parquet` file using:

```python
import polars as pl
import pyarrow.parquet as pq
import s3fs

fs = s3fs.S3FileSystem()
bucket = "<YOUR_BUCKET>"
path = "<YOUR_PATH>"

dataset = pq.ParquetDataset(f"s3://{bucket}/{path}", filesystem=fs)
df = pl.from_arrow(dataset.read())
```

## Write

> This content is under construction.
