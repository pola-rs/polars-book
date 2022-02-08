import polars as pl

pl.scan_csv("my_many_files_*.csv").show_graph(output_path="single_df_graph.png", show=False)
