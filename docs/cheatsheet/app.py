import streamlit as st
from pathlib import Path
import base64
import requests

# Initial page config
st.set_page_config(
    page_title='Polars Cheat Sheet',
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    """
    Main function to set up the Streamlit app layout.
    """
    cs_sidebar()
    cs_body()
    return None

# Define img_to_bytes() function
def img_to_bytes(img_url):
    response = requests.get(img_url)
    img_bytes = response.content
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


# Define the cs_sidebar() function
def cs_sidebar():
    """
    Populate the sidebar with various content sections related to Polars.
    """
    st.sidebar.markdown(
        '''[<img src='data:image/svg;base64,{}' class='img-fluid' width=200 >](https://streamlit.io/)'''.format(
            img_to_bytes("https://raw.githubusercontent.com/fralfaro/DS-Cheat-Sheets/main/docs/examples/polars/polars.png")), unsafe_allow_html=True)

    st.sidebar.header('Polars Cheat Sheet')
    st.sidebar.markdown('''
<small>[Polars](https://pola-rs.github.io/polars-book/) is a highly performant DataFrame library for manipulating structured data. The core is written in Rust, but the library is also available in Python. </small>
    ''', unsafe_allow_html=True)

    # Polars installation and import
    st.sidebar.markdown('__Install and import Polars__')
    st.sidebar.code('$ pip install polars')
    st.sidebar.code('''
# Import Polars convention
>>> import polars as pl
''')

    # Creating/reading DataFrames
    st.sidebar.subheader('Creating/reading DataFrames')
    st.sidebar.markdown('__Create DataFrame__')
    st.sidebar.code('''
            # Create a DataFrame
            df = pd.DataFrame(
                {
                    "nrs": [1, 2, 3, None, 5],
                    "names": ["foo", "ham", "spam", "egg", None],
                    "random": [0.3, 0.7, 0.1, 0.9, 0.6],
                    "groups": ["A", "A", "B", "C", "B"],
                }
            )
            ''')
    st.sidebar.markdown('__Read CSV__')
    st.sidebar.code('''
    # Read CSV
    df = pl.read_csv(
        "https://j.mp/iriscsv",
         has_header=True
    )
            ''')
    st.sidebar.markdown('__Read parquet__')
    st.sidebar.code('''
    # Read a Parquet file with selected columns
    df = pd.read_parquet(
        "path.parquet", 
        columns=["select", "columns"]
    )
            ''')

    # Expressions
    st.sidebar.subheader('Expressions')
    st.sidebar.markdown('''
    <small>Polars expressions can be performed in sequence. This improves readability of code. </small>
        ''', unsafe_allow_html=True)
    st.sidebar.code('''
            # Filter rows where 'nrs' column is less than 4,
            # then group by 'groups' column and calculate the sum
            df.filter(pl.col("nrs") < 4).groupby("groups").agg(pl.all().sum())
            ''')



    return None


# Define the cs_body() function
def cs_body():
    """
    Create content sections for the main body of the Streamlit cheat sheet with Polars examples.
    """
    col1, col2, col3 = st.columns(3)  # Create columns for layout

    #######################################
    # COLUMN 1
    #######################################

    # Filter
    col1.subheader("Filter")
    col1.code('''
            # Extract rows where 'random' column is greater than 0.5
            df.filter(pl.col("random") > 0.5)

            # Extract rows where 'groups' is "B" and 'random' is greater than 0.5
            df.filter((pl.col("groups") == "B") & (pl.col("random") > 0.5))
            ''')

    # Sample
    col1.subheader("Sample")
    col1.code('''
            # Randomly select fraction of rows
            df.sample(frac=0.5)

            # Randomly select n rows
            df.sample(n=2)

            # Select first n rows
            df.head(n=2)

            # Select last n rows
            df.tail(n=2)
            ''')

    # Expressions Example
    col1.subheader("Expressions Example")
    col1.code('''
            # Filter rows where 'nrs' column is less than 4,
            # then group by 'groups' column and calculate the sum
            df.filter(pl.col("nrs") < 4).groupby("groups").agg(pl.all().sum())
            ''')

    # Subsets - rows and columns
    col1.subheader("Subsets - rows and columns")
    col1.code('''
    # Select rows 2-4
    df[2:4, :]
    ''')
    col1.code('''
    # Select columns in positions 1 and 3 (first column is 0)
    df[:, [1, 3]]
    ''')
    col1.code('''
    # Select rows meeting logical condition and specific columns
    df[df["random"] > 0.5, ["names", "groups"]]
    ''')



    #######################################
    # COLUMN 2
    #######################################

    # Reshaping Data – Change layout, sorting, renaming
    col1.subheader("Reshaping Data – Change layout, sorting, renaming")
    col1.code('''
            # Append rows of DataFrames
            pl.concat([df, df2])
            ''')
    col1.code('''
            # Append columns of DataFrames
            pl.concat([df, df3], how="horizontal")
            ''')
    col1.code('''
            # Gather columns into rows
            df.melt(id_vars="nrs", value_vars=["names", "groups"])
            ''')
    col1.code('''
            # Spread rows into columns
            df.pivot(values="nrs", index="groups", columns="names")
            ''')
    col1.code('''
            # Order rows by values of a column (low to high)
            df.sort("random")
            ''')
    col1.code('''
            # Order rows by values of a column (high to low)
            df.sort("random", reverse=True)
            ''')
    col1.code('''
            # Rename the columns of a DataFrame
            df.rename({"nrs": "idx"})
            ''')
    col1.code('''
            # Drop columns from DataFrame
            df.drop(["names", "random"])
            ''')

    #######################################
    # COLUMN 3
    #######################################

    # Summarize Data
    col2.subheader("Summarize Data")

    col2.code('''
            # Count number of rows with each unique value of variable
            df["groups"].value_counts()
            ''')

    col2.code('''
            # rows in DataFrame (or df.height)
            len(df) 
            ''')

    col2.code('''
            # Tuple of # of rows, # of columns in DataFrame
            df.shape
            ''')

    col2.code('''
            # of distinct values in a column
            df["groups"].n_unique()
            ''')

    col2.code('''
            # Basic descriptive and statistics for each column
            df.describe()
            ''')

    col2.code('''
            df.select(
                [
                    # Sum values
                    pl.sum("random").alias("sum"),
                    # Minimum value
                    pl.min("random").alias("min"),
                    # Maximum value
                    pl.max("random").alias("max"),
                    # or
                    pl.col("random").max().alias("other_max"),
                    # Standard deviation
                    pl.std("random").alias("std_dev"),
                    # Variance
                    pl.var("random").alias("variance"),
                    # Median
                    pl.median("random").alias("median"),
                    # Mean
                    pl.mean("random").alias("mean"),
                    # Quantile
                    pl.quantile("random", 0.75).alias("quantile_0.75"),
                    # or
                    pl.col("random").quantile(0.75).alias("other_quantile_0.75"),
                    # First value
                    pl.first("random").alias("first"),
                ]
            )
            ''')

    # Group Data
    col2.subheader("Group Data")

    col2.code('''
            # Group by values in column named 'col', returning a GroupBy object
            df.groupby("groups")
            ''')

    col2.code('''
            # All of the aggregation functions from above can be applied to a group as well
            df.groupby(by="groups").agg(
                [
                    # Sum values
                    pl.sum("random").alias("sum"),
                    # Minimum value
                    pl.min("random").alias("min"),
                    # Maximum value
                    pl.max("random").alias("max"),
                    # Standard deviation
                    pl.std("random").alias("std_dev"),
                    # Variance
                    pl.var("random").alias("variance"),
                    # Median
                    pl.median("random").alias("median"),
                    # Mean
                    pl.mean("random").alias("mean"),
                    # Quantile
                    pl.quantile("random", 0.75).alias("quantile_0.75"),
                    # First value
                    pl.first("random").alias("first"),
                ]
            )
            ''')

    col2.code('''
            # Additional GroupBy functions
            df.groupby(by="groups").agg(
                [
                    # Count the number of values in each group
                    pl.count("random").alias("size"),
                    # Sample one element in each group
                    pl.col("names").apply(lambda group_df: group_df.sample(1)),
                ]
            )
            ''')

    # Handling Missing Data
    col3.subheader("Handling Missing Data")

    col3.code('''
            # Drop rows with any column having a null value
            df.drop_nulls()
            ''')

    col3.code('''
            # Replace null values with given value
            df.fill_null(42)
            ''')

    col3.code('''
            # Replace null values using forward strategy
            df.fill_null(strategy="forward")
            # Other fill strategies are "backward", "min", "max", "mean", "zero", and "one"
            ''')

    col3.code('''
            # Replace floating point NaN values with given value
            df.fill_nan(42)
            ''')

    # Combine Data Sets
    col3.subheader("Combine Data Sets")

    col3.code('''
            df4 = pl.DataFrame(
                {
                    "nrs": [1, 2, 5, 6],
                    "animals": ["cheetah", "lion", "leopard", "tiger"],
                }
            )

            # Inner join
            df.join(df4, on="nrs", how="inner")

            # Left join
            df.join(df4, on="nrs", how="left")

            # Outer join
            df.join(df4, on="nrs", how="outer")

            # Anti join
            df.join(df4, on="nrs", how="anti")
            ''')

    # Make New Columns
    col3.subheader("Make New Columns")

    col3.code('''
            # Add a new column to the DataFrame
            df.with_column((pl.col("random") * pl.col("nrs")).alias("product"))
            ''')

    col3.code('''
            # Add several new columns to the DataFrame
            df.with_columns(
                [
                    (pl.col("random") * pl.col("nrs")).alias("product"),
                    pl.col("names").str.lengths().alias("names_lengths"),
                ]
            )
            ''')

    col3.code('''
            # Add a column at index 0 that counts the rows
            df.with_row_count()
            ''')

    # Rolling Functions
    col3.subheader("Rolling Functions")

    col3.code('''
            # Rolling Functions
            df.select(
                [
                    pl.col("random"),
                    # Rolling maximum value
                    pl.col("random").rolling_max(window_size=2).alias("rolling_max"),
                    # Rolling mean value
                    pl.col("random").rolling_mean(window_size=2).alias("rolling_mean"),
                    # Rolling median value
                    pl.col("random")
                    .rolling_median(window_size=2, min_periods=2)
                    .alias("rolling_median"),
                    # ... (other rolling functions)
                ]
            )
            ''')

    # Window Functions
    col3.subheader("Window Functions")
    col3.code('''
            # Window Functions
            df.select(
                [
                    "names",
                    "groups",
                    pl.col("random").sum().over("names").alias("sum_by_names"),
                    pl.col("random").sum().over("groups").alias("sum_by_groups"),
                ]
            )
            ''')


# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
