
# Joins
Joins allow you to combine the data from a left `DataFrame` `df_left` and a right `DataFrame` `df_right`.

## Join strategies
`Polars` supports the following join strategies
- inner
- left
- outer
- cross
- asof
- semi
- anti

The inner,left, outer and cross join strategies are standard and well documented elsewhere. We provide more details on the less familiar asof, semi and anti join strategies below.

### Semi join
Consider the following scenario: a car rental company has a `DataFrame` showing the cars that it owns with each car having a unique `id`. 

The company has another `DataFrame` showing each repair job carried out on a vehicle. 

You want to answer this question: which of the cars have had repairs carried out?

In this case an inner join would produce a `DataFrame` with multiple rows for each car that has had multiple repair jobs. This `DataFrame` must then be filtered to remove duplicate cars.

However, a semi join produces a single row for each car that has had a repair job carried out.

### Anti join
An alternative question might be: which of the cars have **not** had a repair job carried out? An anti join produces a `DataFrame` showing all the cars from `df_cars` where the `id` is not present in the `df_repairs` `DataFrame`.

### Asof join
An asof join is like a left join except that we match on nearest key rather than equal keys.
In `Polars` we can do an asof join with the `join` method and specifying `strategy="asof"`. However, for more flexibility we can use the `join_asof` method.

Consider the following scenario: a stock market broker has a `DataFrame` `df_trades` showing transactions it has made for different stocks. 

The broker has another `DataFrame` `df_quotes` showing prices it has quoted. 

You want to produce a `DataFrame` showing for each trade the most recent quote provided *before* the trade. You do this with `join_asof` (using the default `strategy = backward`).
To avoid joining between trades on one stock with a quote on another you must specify an exact preliminary join on the stock column with `by="stock"`. 

If you want to make sure that only quotes within a certain time range are joined to the trades you can specify the `tolerance` argument. In this case we want to make sure that the last preceding quote is within 5 minutes of the trade.

