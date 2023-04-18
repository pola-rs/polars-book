# Interact with AWS

To read from or write to an AWS bucket, additional dependencies are needed:

<div class="tabbed-blocks">

```shell-python
$ pip install s3fs
```

```shell-rust
$ cargo add aws_sdk_s3 aws_config tokio --features tokio/full
```

</div>

In the next few snippets we'll demonstrate interacting with a `Parquet` file
located on an AWS bucket.

## Read

Load a `.parquet` file using:

<div class="tabbed-blocks">

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

```rust,noplayground
use aws_sdk_s3::Region;

use aws_config::meta::region::RegionProviderChain;
use aws_sdk_s3::Client;
use std::borrow::Cow;

use polars::prelude::*;

#[tokio::main]
async fn main() {
    let bucket = "<YOUR_BUCKET>";
    let path = "<YOUR_PATH>";

    let config = aws_config::from_env().load().await;
    let client = Client::new(&config);

    let req = client.get_object().bucket(bucket).key(path);

    let res = req.clone().send().await.unwrap();
    let bytes = res.body.collect().await.unwrap();
    let bytes = bytes.into_bytes();

    let cursor = std::io::Cursor::new(bytes);

    let df = CsvReader::new(cursor).finish().unwrap();

    println!("{:?}", df);
}
```

</div>

## Write

> This content is under construction.
