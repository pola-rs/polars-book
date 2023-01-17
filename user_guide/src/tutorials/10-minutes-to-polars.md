# 10 Minutes to Polars
 
To help you get started this notebook introduces some of the key concepts that make Polars a powerful data analysis tool. 

The key concepts we meet are:
- fast flexible analysis with the **Expression API** in Polars
- easy **parallel** computations
- automatic **query optimisation** in **lazy mode**
- **streaming** to work with larger-than-memory datasets in Polars

## Importing Polars
We begin by importing polars as `pl`


```python
import polars as pl
```

## Setting configuration options
Before we start exploring a dataset we are going to control how a `DataFrame` is print on the screen. We control configuration using options in `pl.Config` - [see the API docs for the full range](https://pola-rs.github.io/polars/py-polars/html/reference/config.html).

In this notebook we want Polars to:
- print up to 8 rows of each `DataFrame` so we use `pl.Config.set_tbl_rows` and 
- print up to 10 columns of each `DataFrame` so we use `pl.Config.set_tbl_cols`


```python
{{#include ../examples/tutorials/10_minutes_to_polars/creating_a_dataframe.py:3:4}}
```





    polars.cfg.Config



We also want strings to be printed with up to 30 characters 


```python
{{#include ../examples/tutorials/10_minutes_to_polars/creating_a_dataframe.py:6:6}}
```




    polars.cfg.Config



You can find the [full range of configuration options in the API docs](POLARS_PY_REF_GUIDE/config.html).

## Creating a `DataFrame`
Polars can read from a wide range of data formats including CSV, Parquet, Arrow, JSON, Excel and database connections. See the [I/O section of the User Guide](/howcani/io/intro.html) for more information.

For this introduction we use a CSV with the Titanic passenger dataset. This dataset gives details of all the passengers on the Titanic and whether they survived.

We begin by setting the url of the CSV


```python
csv_url = "https://raw.githubusercontent.com/pola-rs/polars-static/master/data/titanic.csv"
```

We read the CSV into a Polars `DataFrame` with the `read_csv` function. 

We then call `head` to print out the first few rows of the `DataFrame`


```python
{{#include ../examples/tutorials/10_minutes_to_polars/creating_a_dataframe.py:10:10}}
print(df.head(3))
```
Each row of this `DataFrame` has details about a passenger on the Titanic including the class they travelled in (`Pclass`), their name (`Name`) and `Age`.

We save this CSV to a local file for use later in the tutorial


```python
csv_file = "titanic.csv"
df.write_csv(csv_file)
```

When we print out a `DataFrame` we get the shape and the dtype of each column below the column name.

A Polars `DataFrame` does not have an index. The lack of an index saves developer effort in setting and resetting the index.

## Accessing and transforming data

### Using square brackets

While you can use square brackets to select rows and columns in Polars...


```python
df[:3,["Pclass","Name","Age"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (3, 3)</small>
<thead>
<tr>
<th>
Pclass
</th>
<th>
Name
</th>
<th>
Age
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
str
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
3
</td>
<td>
&quot;Braund, Mr. Owen Harris&quot;
</td>
<td>
22.0
</td>
</tr>
<tr>
<td>
1
</td>
<td>
&quot;Cumings, Mrs. John Bradley (F...
</td>
<td>
38.0
</td>
</tr>
<tr>
<td>
3
</td>
<td>
&quot;Heikkinen, Miss. Laina&quot;
</td>
<td>
26.0
</td>
</tr>
</tbody>
</table>
</div>



...this square bracket approach means that you won't get all the benefits of parallelisation, query optimisation and scalability that we see below. 

To really take advantage of Polars we use the Expression API to access and transform data.

### Selecting and transforming columns with the Expression API

We see a first example of the Expression API here where we select the `Pclass`, `Name` and `Age` columns inside a `select` statement


```python
(
    df
    .select(
        [
            pl.col("Pclass"),
            pl.col("Name"),
            pl.col("Age"),
        ]
    )
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (891, 3)</small>
<thead>
<tr>
<th>
Pclass
</th>
<th>
Name
</th>
<th>
Age
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
str
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
3
</td>
<td>
&quot;Braund, Mr. Owen Harris&quot;
</td>
<td>
22.0
</td>
</tr>
<tr>
<td>
1
</td>
<td>
&quot;Cumings, Mrs. John Bradley (Florence Briggs Thayer)&quot;
</td>
<td>
38.0
</td>
</tr>
<tr>
<td>
3
</td>
<td>
&quot;Heikkinen, Miss. Laina&quot;
</td>
<td>
26.0
</td>
</tr>
<tr>
<td>
1
</td>
<td>
&quot;Futrelle, Mrs. Jacques Heath (Lily May Peel)&quot;
</td>
<td>
35.0
</td>
</tr>
<tr>
<td>
...
</td>
<td>
...
</td>
<td>
...
</td>
</tr>
<tr>
<td>
1
</td>
<td>
&quot;Graham, Miss. Margaret Edith&quot;
</td>
<td>
19.0
</td>
</tr>
<tr>
<td>
3
</td>
<td>
&quot;Johnston, Miss. Catherine Helen &quot;Carrie&quot;&quot;
</td>
<td>
null
</td>
</tr>
<tr>
<td>
1
</td>
<td>
&quot;Behr, Mr. Karl Howell&quot;
</td>
<td>
26.0
</td>
</tr>
<tr>
<td>
3
</td>
<td>
&quot;Dooley, Mr. Patrick&quot;
</td>
<td>
32.0
</td>
</tr>
</tbody>
</table>
</div>



In the Expression API we begin by using `pl.col` to select to a column. We call the operation on each column an **expression**

### Transforming columns in the Expression API 
However, the Expression API allows us not only to select columns but also to transform them.

Here we select the same three columns, but with some transformations in each expression before we return them:
- we convert the integers in `Pclass` to the utf-8 string dtype with `cast`
- we get the number of words in each name with `str.to_lowercase` and
- we round off the age to the nearest whole number with `round`


```python
(
    df
    .select(
        [
            pl.col("Pclass").cast(pl.Utf8),
            pl.col("Name").str.to_lowercase(),
            pl.col("Age").round(2)
        ]
    )
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (891, 3)</small>
<thead>
<tr>
<th>
Pclass
</th>
<th>
Name
</th>
<th>
Age
</th>
</tr>
<tr>
<td>
str
</td>
<td>
str
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
&quot;3&quot;
</td>
<td>
&quot;braund, mr. owen harris&quot;
</td>
<td>
22.0
</td>
</tr>
<tr>
<td>
&quot;1&quot;
</td>
<td>
&quot;cumings, mrs. john bradley (florence briggs thayer)&quot;
</td>
<td>
38.0
</td>
</tr>
<tr>
<td>
&quot;3&quot;
</td>
<td>
&quot;heikkinen, miss. laina&quot;
</td>
<td>
26.0
</td>
</tr>
<tr>
<td>
&quot;1&quot;
</td>
<td>
&quot;futrelle, mrs. jacques heath (lily may peel)&quot;
</td>
<td>
35.0
</td>
</tr>
<tr>
<td>
...
</td>
<td>
...
</td>
<td>
...
</td>
</tr>
<tr>
<td>
&quot;1&quot;
</td>
<td>
&quot;graham, miss. margaret edith&quot;
</td>
<td>
19.0
</td>
</tr>
<tr>
<td>
&quot;3&quot;
</td>
<td>
&quot;johnston, miss. catherine helen &quot;carrie&quot;&quot;
</td>
<td>
null
</td>
</tr>
<tr>
<td>
&quot;1&quot;
</td>
<td>
&quot;behr, mr. karl howell&quot;
</td>
<td>
26.0
</td>
</tr>
<tr>
<td>
&quot;3&quot;
</td>
<td>
&quot;dooley, mr. patrick&quot;
</td>
<td>
32.0
</td>
</tr>
</tbody>
</table>
</div>



### Parallel operations

In this example we passed a `list` of expressions to `select`. When we have multiple expressions Polars runs them in parallel. This is one example of how Polars handles parallelisation automatically.

### Chaining expressions
We chain expressions together to do multi-stage transformations on a column. 

In this example we output the name and count the number of words in each name by:
- splitting the `Name` column into a list of words with `str.split` and then
- counting the length of each list with `arr.lengths`

We add the word count as a new column by giving it an `alias` at the end of the expression


```python
(
    df
    .select(
        [
            pl.col("Name"),
            pl.col("Name").str.split(" ").arr.lengths().alias("Name_word_count"),
        ]
    )
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (891, 2)</small>
<thead>
<tr>
<th>
Name
</th>
<th>
Name_word_count
</th>
</tr>
<tr>
<td>
str
</td>
<td>
u32
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
&quot;Braund, Mr. Owen Harris&quot;
</td>
<td>
4
</td>
</tr>
<tr>
<td>
&quot;Cumings, Mrs. John Bradley (Florence Briggs Thayer)&quot;
</td>
<td>
7
</td>
</tr>
<tr>
<td>
&quot;Heikkinen, Miss. Laina&quot;
</td>
<td>
3
</td>
</tr>
<tr>
<td>
&quot;Futrelle, Mrs. Jacques Heath (Lily May Peel)&quot;
</td>
<td>
7
</td>
</tr>
<tr>
<td>
...
</td>
<td>
...
</td>
</tr>
<tr>
<td>
&quot;Graham, Miss. Margaret Edith&quot;
</td>
<td>
4
</td>
</tr>
<tr>
<td>
&quot;Johnston, Miss. Catherine Helen &quot;Carrie&quot;&quot;
</td>
<td>
5
</td>
</tr>
<tr>
<td>
&quot;Behr, Mr. Karl Howell&quot;
</td>
<td>
4
</td>
</tr>
<tr>
<td>
&quot;Dooley, Mr. Patrick&quot;
</td>
<td>
3
</td>
</tr>
</tbody>
</table>
</div>



## Adding a column
In the examples above we use `select` to return a subset of columns. To add a new column to the full `DataFrame` we use `with_column`


```python
(
    df
    .with_column(
            pl.col("Name").str.split(" ").arr.lengths().alias("Name_word_count"),
    )
    .head(3)
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (3, 10)</small>
<thead>
<tr>
<th>
Id
</th>
<th>
Survived
</th>
<th>
Pclass
</th>
<th>
Name
</th>
<th>
Sex
</th>
<th>
Age
</th>
<th>
SibSp
</th>
<th>
Parch
</th>
<th>
Fare
</th>
<th>
Name_word_count
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
i64
</td>
<td>
i64
</td>
<td>
str
</td>
<td>
str
</td>
<td>
f64
</td>
<td>
i64
</td>
<td>
i64
</td>
<td>
f64
</td>
<td>
u32
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
1
</td>
<td>
0
</td>
<td>
3
</td>
<td>
&quot;Braund, Mr. Owen Harris&quot;
</td>
<td>
&quot;male&quot;
</td>
<td>
22.0
</td>
<td>
1
</td>
<td>
0
</td>
<td>
7.25
</td>
<td>
4
</td>
</tr>
<tr>
<td>
2
</td>
<td>
1
</td>
<td>
1
</td>
<td>
&quot;Cumings, Mrs. John Bradley (Florence Briggs Thayer)&quot;
</td>
<td>
&quot;female&quot;
</td>
<td>
38.0
</td>
<td>
1
</td>
<td>
0
</td>
<td>
71.28
</td>
<td>
7
</td>
</tr>
<tr>
<td>
3
</td>
<td>
1
</td>
<td>
3
</td>
<td>
&quot;Heikkinen, Miss. Laina&quot;
</td>
<td>
&quot;female&quot;
</td>
<td>
26.0
</td>
<td>
0
</td>
<td>
0
</td>
<td>
7.93
</td>
<td>
3
</td>
</tr>
</tbody>
</table>
</div>



We add multiple new columns using `with_columns`


```python
(
    df
    .with_columns(
        [
            pl.col("Name").str.split(" ").arr.lengths().alias("Name_word_count"),
            pl.col("Fare").round(1).alias("Fare_rounded")
        ]
    )
    .head(3)
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (3, 11)</small>
<thead>
<tr>
<th>
Id
</th>
<th>
Survived
</th>
<th>
Pclass
</th>
<th>
Name
</th>
<th>
Sex
</th>
<th>
...
</th>
<th>
SibSp
</th>
<th>
Parch
</th>
<th>
Fare
</th>
<th>
Name_word_count
</th>
<th>
Fare_rounded
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
i64
</td>
<td>
i64
</td>
<td>
str
</td>
<td>
str
</td>
<td>
...
</td>
<td>
i64
</td>
<td>
i64
</td>
<td>
f64
</td>
<td>
u32
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
1
</td>
<td>
0
</td>
<td>
3
</td>
<td>
&quot;Braund, Mr. Owen Harris&quot;
</td>
<td>
&quot;male&quot;
</td>
<td>
...
</td>
<td>
1
</td>
<td>
0
</td>
<td>
7.25
</td>
<td>
4
</td>
<td>
7.3
</td>
</tr>
<tr>
<td>
2
</td>
<td>
1
</td>
<td>
1
</td>
<td>
&quot;Cumings, Mrs. John Bradley (Florence Briggs Thayer)&quot;
</td>
<td>
&quot;female&quot;
</td>
<td>
...
</td>
<td>
1
</td>
<td>
0
</td>
<td>
71.28
</td>
<td>
7
</td>
<td>
71.3
</td>
</tr>
<tr>
<td>
3
</td>
<td>
1
</td>
<td>
3
</td>
<td>
&quot;Heikkinen, Miss. Laina&quot;
</td>
<td>
&quot;female&quot;
</td>
<td>
...
</td>
<td>
0
</td>
<td>
0
</td>
<td>
7.93
</td>
<td>
3
</td>
<td>
7.9
</td>
</tr>
</tbody>
</table>
</div>



Square brackets **cannot** be used to add new columns, so the following does not work
```python
df["Fare_rounded"] = df["Fare"].round(1)
```


### Filtering a `DataFrame`

We filter a `DataFrame` by applying a condition in an expression.

In this example we find all the passengers over 70 years of age


```python
(
    df
    .filter(
        pl.col("Age") > 70
    )
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (5, 9)</small>
<thead>
<tr>
<th>
Id
</th>
<th>
Survived
</th>
<th>
Pclass
</th>
<th>
Name
</th>
<th>
Sex
</th>
<th>
Age
</th>
<th>
SibSp
</th>
<th>
Parch
</th>
<th>
Fare
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
i64
</td>
<td>
i64
</td>
<td>
str
</td>
<td>
str
</td>
<td>
f64
</td>
<td>
i64
</td>
<td>
i64
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
97
</td>
<td>
0
</td>
<td>
1
</td>
<td>
&quot;Goldschmidt, Mr. George B&quot;
</td>
<td>
&quot;male&quot;
</td>
<td>
71.0
</td>
<td>
0
</td>
<td>
0
</td>
<td>
34.65
</td>
</tr>
<tr>
<td>
117
</td>
<td>
0
</td>
<td>
3
</td>
<td>
&quot;Connors, Mr. Patrick&quot;
</td>
<td>
&quot;male&quot;
</td>
<td>
70.5
</td>
<td>
0
</td>
<td>
0
</td>
<td>
7.75
</td>
</tr>
<tr>
<td>
494
</td>
<td>
0
</td>
<td>
1
</td>
<td>
&quot;Artagaveytia, Mr. Ramon&quot;
</td>
<td>
&quot;male&quot;
</td>
<td>
71.0
</td>
<td>
0
</td>
<td>
0
</td>
<td>
49.5
</td>
</tr>
<tr>
<td>
631
</td>
<td>
1
</td>
<td>
1
</td>
<td>
&quot;Barkworth, Mr. Algernon Henry Wilson&quot;
</td>
<td>
&quot;male&quot;
</td>
<td>
80.0
</td>
<td>
0
</td>
<td>
0
</td>
<td>
30.0
</td>
</tr>
<tr>
<td>
852
</td>
<td>
0
</td>
<td>
3
</td>
<td>
&quot;Svensson, Mr. Johan&quot;
</td>
<td>
&quot;male&quot;
</td>
<td>
74.0
</td>
<td>
0
</td>
<td>
0
</td>
<td>
7.78
</td>
</tr>
</tbody>
</table>
</div>



We can specify multiple conditions with the `&` operator


```python
(
    df
    .filter(
        (pl.col("Age") > 70) & (pl.col("Pclass") == 3)
    )
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (2, 9)</small>
<thead>
<tr>
<th>
Id
</th>
<th>
Survived
</th>
<th>
Pclass
</th>
<th>
Name
</th>
<th>
Sex
</th>
<th>
Age
</th>
<th>
SibSp
</th>
<th>
Parch
</th>
<th>
Fare
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
i64
</td>
<td>
i64
</td>
<td>
str
</td>
<td>
str
</td>
<td>
f64
</td>
<td>
i64
</td>
<td>
i64
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
117
</td>
<td>
0
</td>
<td>
3
</td>
<td>
&quot;Connors, Mr. Patrick&quot;
</td>
<td>
&quot;male&quot;
</td>
<td>
70.5
</td>
<td>
0
</td>
<td>
0
</td>
<td>
7.75
</td>
</tr>
<tr>
<td>
852
</td>
<td>
0
</td>
<td>
3
</td>
<td>
&quot;Svensson, Mr. Johan&quot;
</td>
<td>
&quot;male&quot;
</td>
<td>
74.0
</td>
<td>
0
</td>
<td>
0
</td>
<td>
7.78
</td>
</tr>
</tbody>
</table>
</div>



## Analytics
We begin by getting an overview of the `DataFrame` with `describe`


```python
(
    df
    .describe()
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (7, 10)</small>
<thead>
<tr>
<th>
describe
</th>
<th>
Id
</th>
<th>
Survived
</th>
<th>
Pclass
</th>
<th>
Name
</th>
<th>
Sex
</th>
<th>
Age
</th>
<th>
SibSp
</th>
<th>
Parch
</th>
<th>
Fare
</th>
</tr>
<tr>
<td>
str
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
str
</td>
<td>
str
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
&quot;count&quot;
</td>
<td>
891.0
</td>
<td>
891.0
</td>
<td>
891.0
</td>
<td>
&quot;891&quot;
</td>
<td>
&quot;891&quot;
</td>
<td>
891.0
</td>
<td>
891.0
</td>
<td>
891.0
</td>
<td>
891.0
</td>
</tr>
<tr>
<td>
&quot;null_count&quot;
</td>
<td>
0.0
</td>
<td>
0.0
</td>
<td>
0.0
</td>
<td>
&quot;0&quot;
</td>
<td>
&quot;0&quot;
</td>
<td>
177.0
</td>
<td>
0.0
</td>
<td>
0.0
</td>
<td>
0.0
</td>
</tr>
<tr>
<td>
&quot;mean&quot;
</td>
<td>
446.0
</td>
<td>
0.383838
</td>
<td>
2.308642
</td>
<td>
null
</td>
<td>
null
</td>
<td>
29.699118
</td>
<td>
0.523008
</td>
<td>
0.381594
</td>
<td>
32.204994
</td>
</tr>
<tr>
<td>
&quot;std&quot;
</td>
<td>
257.353842
</td>
<td>
0.486592
</td>
<td>
0.836071
</td>
<td>
null
</td>
<td>
null
</td>
<td>
14.526497
</td>
<td>
1.102743
</td>
<td>
0.806057
</td>
<td>
49.693399
</td>
</tr>
<tr>
<td>
&quot;min&quot;
</td>
<td>
1.0
</td>
<td>
0.0
</td>
<td>
1.0
</td>
<td>
&quot;Abbing, Mr. Anthony&quot;
</td>
<td>
&quot;female&quot;
</td>
<td>
0.42
</td>
<td>
0.0
</td>
<td>
0.0
</td>
<td>
0.0
</td>
</tr>
<tr>
<td>
&quot;max&quot;
</td>
<td>
891.0
</td>
<td>
1.0
</td>
<td>
3.0
</td>
<td>
&quot;van Melkebeke, Mr. Philemon&quot;
</td>
<td>
&quot;male&quot;
</td>
<td>
80.0
</td>
<td>
8.0
</td>
<td>
6.0
</td>
<td>
512.33
</td>
</tr>
<tr>
<td>
&quot;median&quot;
</td>
<td>
446.0
</td>
<td>
0.0
</td>
<td>
3.0
</td>
<td>
null
</td>
<td>
null
</td>
<td>
28.0
</td>
<td>
0.0
</td>
<td>
0.0
</td>
<td>
14.45
</td>
</tr>
</tbody>
</table>
</div>



The output of `describe` shows us how many records there are, how many `null` values and some key statistics.

### Value counts on a column
We use `value_counts` to count occurences of values in a column.

In this example we count how many passengers there are in each class with `value_counts`


```python
(
    df["Pclass"]
    .value_counts()
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (3, 2)</small>
<thead>
<tr>
<th>
Pclass
</th>
<th>
counts
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
u32
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
1
</td>
<td>
216
</td>
</tr>
<tr>
<td>
3
</td>
<td>
491
</td>
</tr>
<tr>
<td>
2
</td>
<td>
184
</td>
</tr>
</tbody>
</table>
</div>



### Groupby and aggregations
Here we look at passenger survival by class.
- We first group by the `Survived` and the `Pclass` columns 
- We then aggregate in `agg` by counting the number of passengers in each group


```python
(
    df
    .groupby(["Survived","Pclass"])
    .agg(
        pl.col("Id").count().alias("counts")
    )
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (6, 3)</small>
<thead>
<tr>
<th>
Survived
</th>
<th>
Pclass
</th>
<th>
counts
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
i64
</td>
<td>
u32
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
3
</td>
<td>
372
</td>
</tr>
<tr>
<td>
0
</td>
<td>
1
</td>
<td>
80
</td>
</tr>
<tr>
<td>
1
</td>
<td>
2
</td>
<td>
87
</td>
</tr>
<tr>
<td>
0
</td>
<td>
2
</td>
<td>
97
</td>
</tr>
<tr>
<td>
1
</td>
<td>
1
</td>
<td>
136
</td>
</tr>
<tr>
<td>
1
</td>
<td>
3
</td>
<td>
119
</td>
</tr>
</tbody>
</table>
</div>



We use the Expression API for each aggregation in `agg`.

Groupby operations in Polars are fast because Polars has a parallel algorithm for getting the groupby keys. Aggregations are also fast because Polars runs multiple expressions in `agg` in parallel.

### Window operations
If we want to add a column that reflects not just data from that row but from a related group of rows we use a window operation. Windows occur in many contexts including rolling or temporal statistics and Polars covers these use cases.

One example of a window operation is when we want the percentage breakdown within a group. We use the `over` expression to do this window operation.

For example, here we use `over` to calculate what percentage of passengers in each class survived 


```python
survived_percentage_df = (
    df
    # Groupby Survived and Pclass
    .groupby(["Survived","Pclass"])
    # Count the number of passengers in each group
    .agg(
        pl.col("Id").count().alias("counts")
    )
    # Divide the number of passengers in each group by the total passengers in each class
    .with_column(
        100*(
            pl.col("counts")/pl.col("counts").sum().over("Pclass")
        )
        .alias("% Survived")
    )
    # Sort the output
    .sort(["Pclass","Survived"],reverse=True)
)
survived_percentage_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (6, 4)</small>
<thead>
<tr>
<th>
Survived
</th>
<th>
Pclass
</th>
<th>
counts
</th>
<th>
% Survived
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
i64
</td>
<td>
u32
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
1
</td>
<td>
3
</td>
<td>
119
</td>
<td>
24.236253
</td>
</tr>
<tr>
<td>
0
</td>
<td>
3
</td>
<td>
372
</td>
<td>
75.763747
</td>
</tr>
<tr>
<td>
1
</td>
<td>
2
</td>
<td>
87
</td>
<td>
47.282609
</td>
</tr>
<tr>
<td>
0
</td>
<td>
2
</td>
<td>
97
</td>
<td>
52.717391
</td>
</tr>
<tr>
<td>
1
</td>
<td>
1
</td>
<td>
136
</td>
<td>
62.962963
</td>
</tr>
<tr>
<td>
0
</td>
<td>
1
</td>
<td>
80
</td>
<td>
37.037037
</td>
</tr>
</tbody>
</table>
</div>



## Lazy mode and query optimisation
In the examples above we work in eager mode. In eager mode Polars runs each part of a query step-by-step.

Polars has a powerful feature called lazy mode. In this mode Polars looks at a query as a whole to make a query graph. 

Before running the code Polars passes the query graph through its optimiser to see if there ways to make the query faster.

When working with a CSV we can work in lazy mode instead of eager mode by replacing `read_csv` with `scan_csv`


```python
(
    pl.scan_csv(csv_file)
    .groupby(["Survived","Pclass"])
    .agg(
        pl.col("Id").count().alias("counts")
    )
)
```




<h4>NAIVE QUERY PLAN</h4><p>run <b>LazyFrame.show_graph()</b> to see the optimized version</p><?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 6.0.1 (20220911.1526)
 -->
<!-- Title: polars_query Pages: 1 -->
<svg width="243pt" height="150pt"
 viewBox="0.00 0.00 243.00 150.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 146)">
<title>polars_query</title>
<polygon fill="white" stroke="none" points="-4,4 -4,-146 239,-146 239,4 -4,4"/>
<!-- AGG [col(&quot;Id&quot;).count().alias(&quot;counts&quot;)]
BY
[col(&quot;Survived&quot;),col(&quot;Pclass&quot;)] [(0, 0)] [(0, 0)] -->
<g id="node1" class="node">
<title>AGG [col(&quot;Id&quot;).count().alias(&quot;counts&quot;)]
BY
[col(&quot;Survived&quot;),col(&quot;Pclass&quot;)] [(0, 0)] [(0, 0)]</title>
<polygon fill="none" stroke="black" points="235,-142 0,-142 0,-89 235,-89 235,-142"/>
<text text-anchor="middle" x="117.5" y="-126.8" font-family="Times,serif" font-size="14.00">AGG [col(&quot;Id&quot;).count().alias(&quot;counts&quot;)]</text>
<text text-anchor="middle" x="117.5" y="-111.8" font-family="Times,serif" font-size="14.00">BY</text>
<text text-anchor="middle" x="117.5" y="-96.8" font-family="Times,serif" font-size="14.00">[col(&quot;Survived&quot;),col(&quot;Pclass&quot;)] [(0, 0)]</text>
</g>
<!-- CSV SCAN titanic_mod.csv;
π */9;
σ &#45;; [(0, 1)] -->
<g id="node2" class="node">
<title>CSV SCAN titanic_mod.csv;
π */9;
σ &#45;; [(0, 1)]</title>
<polygon fill="none" stroke="black" points="206,-53 29,-53 29,0 206,0 206,-53"/>
<text text-anchor="middle" x="117.5" y="-37.8" font-family="Times,serif" font-size="14.00">CSV SCAN titanic_mod.csv;</text>
<text text-anchor="middle" x="117.5" y="-22.8" font-family="Times,serif" font-size="14.00">π */9;</text>
<text text-anchor="middle" x="117.5" y="-7.8" font-family="Times,serif" font-size="14.00">σ &#45;;</text>
</g>
<!-- AGG [col(&quot;Id&quot;).count().alias(&quot;counts&quot;)]
BY
[col(&quot;Survived&quot;),col(&quot;Pclass&quot;)] [(0, 0)] [(0, 0)]&#45;&#45;CSV SCAN titanic_mod.csv;
π */9;
σ &#45;; [(0, 1)] -->
<g id="edge1" class="edge">
<title>AGG [col(&quot;Id&quot;).count().alias(&quot;counts&quot;)]
BY
[col(&quot;Survived&quot;),col(&quot;Pclass&quot;)] [(0, 0)] [(0, 0)]&#45;&#45;CSV SCAN titanic_mod.csv;
π */9;
σ &#45;; [(0, 1)]</title>
<path fill="none" stroke="black" d="M117.5,-88.87C117.5,-77.64 117.5,-64.49 117.5,-53.25"/>
</g>
</g>
</svg>




The output of a lazy query is a `LazyFrame` and we see the graph of the unoptimized query plan when we output a `LazyFrame`.

### Query optimiser
We can see the optimised query plan that Polars will actually run by adding `describe_optimized_plan` at the end of the query


```python
print(
    pl.scan_csv(csv_file)
    .groupby(["Survived","Pclass"])
    .agg(
        pl.col("Id").count().alias("counts")
    )
    .describe_optimized_plan()
)
```

      Aggregate
      	[col("Id").count().alias("counts")] BY [col("Survived"), col("Pclass")] FROM
      	  CSV SCAN titanic_mod.csv
      PROJECT 3/9 COLUMNS
      SELECTION: None
    
    


### Projection pushdown optimisation
In this example Polars has identified an optimisation and we see this on the second last line of the optimised query plan:
```python
PROJECT 3/12 COLUMNS
```
There are 12 columns in the CSV, but the query optimiser sees that only 3 of these columns are required for the query. When the query is evaluated Polars will `PROJECT` 3 out of 12 columns. This means that Polars will only read the 3 required columns from the CSV. 

This optimisation is called a *projection pushdown*. This projection saves memory and computation time.

You can also see the optimised query plan as a graph (if you have graphviz installed)


```python
(
    pl.scan_csv(csv_file)
    .groupby(["Survived","Pclass"])
    .agg(
        pl.col("Id").count().alias("counts")
    )
    .show_graph()
)
```


    
![svg](10-minutes-to-polars_files/10-minutes-to-polars_44_0.svg)
    


### Predicate pushdown optimisation

A different optimisation happens when we add a `filter` to a query. In this case we want the same analysis of survival by class but only for passengers over 50


```python
print(
    pl.scan_csv(csv_file)
    # Add a filter for passengers over 50
    .filter(pl.col("Age") > 50)
    .groupby(["Survived","Pclass"])
    .agg(
        pl.col("Id").count().alias("counts")
    )
    .describe_optimized_plan()
)
```

      Aggregate
      	[col("Id").count().alias("counts")] BY [col("Survived"), col("Pclass")] FROM
      	  CSV SCAN titanic_mod.csv
      PROJECT 4/9 COLUMNS
      SELECTION: Some([(col("Age")) > (50f64)])
    
    


In this example the query optimiser has seen that:
- 4 out of 12 columns are now required as we also do a filter on `Age`: `PROJECT 4/12 COLUMNS` and
- only passengers over 50 should be selected: `SELECTION: Some([(col("Age")) > (50f64)])`

This optimisation with a filter is called a *predicate pushdown* where the predicate is the condition 
```python
pl.col("Age") > 50
```

These optimisations are applied as Polars reads the CSV file so the whole dataset is not read into memory.

### Query evaluation

#### Full evaluation
To evaluate the query for all output rows we call `collect` 


```python
(
    pl.scan_csv(csv_file)
    .filter(pl.col("Age") > 50)
    .groupby(["Survived","Pclass"])
    .agg(
        pl.col("Id").count().alias("counts")
    )
    .collect()
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (6, 3)</small>
<thead>
<tr>
<th>
Survived
</th>
<th>
Pclass
</th>
<th>
counts
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
i64
</td>
<td>
u32
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
3
</td>
<td>
9
</td>
</tr>
<tr>
<td>
0
</td>
<td>
1
</td>
<td>
21
</td>
</tr>
<tr>
<td>
1
</td>
<td>
2
</td>
<td>
3
</td>
</tr>
<tr>
<td>
0
</td>
<td>
2
</td>
<td>
12
</td>
</tr>
<tr>
<td>
1
</td>
<td>
1
</td>
<td>
18
</td>
</tr>
<tr>
<td>
1
</td>
<td>
3
</td>
<td>
1
</td>
</tr>
</tbody>
</table>
</div>



#### Limited evaluation

During development with a large dataset it may be better to limit evaluation to a smaller number of output rows. We can do this by replacing `collect` with `fetch`


```python
(
    pl.scan_csv(csv_file)
    .filter(pl.col("Age") > 50)
    .groupby(["Survived","Pclass"])
    .agg(
        pl.col("Id").count().alias("counts")
    )
    .fetch(3)
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (3, 3)</small>
<thead>
<tr>
<th>
Survived
</th>
<th>
Pclass
</th>
<th>
counts
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
i64
</td>
<td>
u32
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
1
</td>
<td>
1
</td>
</tr>
<tr>
<td>
1
</td>
<td>
2
</td>
<td>
1
</td>
</tr>
<tr>
<td>
1
</td>
<td>
1
</td>
<td>
1
</td>
</tr>
</tbody>
</table>
</div>



Calling `fetch` is similar to a `LIMIT` clause in a SQL query.

## Streaming larger-than-memory datasets
By default Polars reads your full dataset into memory when evaluating a lazy query. 

However, if your dataset is too large to fit into memory Polars can run many core operations in *streaming* mode. With streaming Polars processes your query in batches rather than all at once. This allows Polars to scale to larger-than-memory datasets.

To enable streaming we pass the `streaming = True` argument to `collect`


```python
(
    pl.scan_csv(csvFile)
    .filter(pl.col("Age") > 50)
    .groupby(["Survived","Pclass"])
    .agg(
        pl.col("Id").count().alias("counts")
    )
    .collect(streaming = True)
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

    .dataframe td {
        white-space: pre;
    }

    .dataframe td {
        padding-top: 0;
    }

    .dataframe td {
        padding-bottom: 0;
    }

    .dataframe td {
        line-height: 95%;
    }
</style>
<table border="1" class="dataframe" >
<small>shape: (6, 3)</small>
<thead>
<tr>
<th>
Survived
</th>
<th>
Pclass
</th>
<th>
counts
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
i64
</td>
<td>
u32
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
2
</td>
<td>
12
</td>
</tr>
<tr>
<td>
0
</td>
<td>
1
</td>
<td>
21
</td>
</tr>
<tr>
<td>
1
</td>
<td>
3
</td>
<td>
1
</td>
</tr>
<tr>
<td>
1
</td>
<td>
2
</td>
<td>
3
</td>
</tr>
<tr>
<td>
0
</td>
<td>
3
</td>
<td>
9
</td>
</tr>
<tr>
<td>
1
</td>
<td>
1
</td>
<td>
18
</td>
</tr>
</tbody>
</table>
</div>



## Summary
This notebook has been a quick overview of the key ideas that make Polars a powerful data analysis tool:
- expressions allow us to write complex transformations concisely and run them in parallel
- lazy mode allows Polars apply query optimisations that reduce memory usage and computation time
- streaming lets us process larger-than-memory datasets

## Next steps
The next step for you is to try Polars on your own data while going through this User Guide.

If you want more information on each function along with an example of use see the [API reference docs](https://pola-rs.github.io/polars/py-polars/html/reference/).

StackOverflow is a great place to start if you need help. There are many Polars questions on there already and your question might already by answered. If you need to ask a new questions you greatly improve your chances of getting help if you provide a minimal working example with some sample inputs, target outputs and your own best effort [as in this example](https://stackoverflow.com/questions/74562243/how-to-perform-split-merge-melt-with-python-and-polars). 

You should also [check in with the Polars community on Discord](https://discord.com/invite/4UfP5cfBE7). This is a great place to chat about how you are using Polars and how you think it could develop.


```python

```
