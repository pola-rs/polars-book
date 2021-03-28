# Reading a Parquet file from AWS s3

To read a parquet file from s3, you'll need to install additional dependencies:

* `$ pip install s3fs`

Next we can load a `parquet` file from aws like this:

```python
import s3fs
import polars as pl
import pyarrow.parquet as pq

fs = s3fs.S3FileSystem()
bucket = "your-bucket"
path = "your-path"

# load dataset
p_dataset = pq.ParquetDataset(
    f"s3://{bucket}/{path}",
    filesystem=fs
)

# read and convert to DataFrame
df = pl.from_arrow(p_dataset.read())
```
