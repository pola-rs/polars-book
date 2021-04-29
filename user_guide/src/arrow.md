# Arrow interoperability

Arrow is rapidly becoming the defacto standard of columnar data. This means that support for Arrow is growing 
rapidly, in languages and in tools. Due to the great effort that's being put in the format, using is Arrow is likely
fastest way to:

* Read en write parquet formatted files
* Read csv into columnar data
* Sending columnar data over the wire (Arrow IPC)

Polars uses Arrow's memory buffers as the most basic building block for `Series`. This means that we exchange 
data between Polars and Arrow zero copy. This means that where arrow performs well, Polars also does. 

Interoperability with Arrow can be achieved with the following function/ methods:

* [convert a DataFrame to arrow](POLARS_API_LINK/frame.html#polars.frame.DataFrame.to_arrow)
* [convert a Series to arrow](POLARS_API_LINK/series.html#polars.series.Series.to_arrow)
* [read from arrow data structure](POLARS_API_LINK//functions.html#polars.functions.from_arrow)
