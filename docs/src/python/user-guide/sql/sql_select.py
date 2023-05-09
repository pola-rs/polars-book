# --8<-- [start:setup]
import polars as pl

# --8<-- [end:setup]


# --8<-- [start:df]
df = pl.DataFrame(
    {
        "city": [
            "New York",
            "Los Angeles",
            "Chicago",
            "Houston",
            "Phoenix",
            "Amsterdam",
        ],
        "country": ["USA", "USA", "USA", "USA", "USA", "Netherlands"],
        "population": [8399000, 3997000, 2705000, 2320000, 1680000, 900000],
    }
).lazy()

ctx = pl.SQLContext()
ctx.register("population", df)

print(ctx.query("SELECT * FROM population"))
# --8<-- [end:df]

# --8<-- [start:groupby]
result = ctx.query(
    """
        SELECT country, AVG(population) as avg_population
        FROM population
        GROUP BY country 
    """
)
print(result)
# --8<-- [end:groupby]


# --8<-- [start:orderby]
result = ctx.query(
    """
        SELECT city, population
        FROM population
        ORDER BY population 
    """
)
print(result)
# --8<-- [end:orderby]

# --8<-- [start:join]
income = pl.DataFrame(
    {
        "city": [
            "New York",
            "Los Angeles",
            "Chicago",
            "Houston",
            "Amsterdam",
            "Rotterdam",
            "Utrecht",
        ],
        "country": [
            "USA",
            "USA",
            "USA",
            "USA",
            "Netherlands",
            "Netherlands",
            "Netherlands",
        ],
        "income": [55000, 62000, 48000, 52000, 42000, 38000, 41000],
    }
).lazy()
ctx.register("income", income)
result = ctx.query(
    """
        SELECT country, city, income, population
        FROM population
        LEFT JOIN income on population.city = income.city
    """
)
print(result)
# --8<-- [end:join]


# --8<-- [start:functions]
result = ctx.query(
    """
        SELECT city, population
        FROM population
        WHERE STARTS_WITH(country,'U')
    """
)
print(result)
# --8<-- [end:functions]

# --8<-- [start:tablefunctions]
result = ctx.query(
    """
        SELECT *
        FROM read_csv('docs/src/data/iris.csv')
    """
)
print(result)
# --8<-- [end:tablefunctions]
