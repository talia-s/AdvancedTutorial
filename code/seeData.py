import polars as pl
df = pl.read_parquet("/fast_scratch_1/TRISEP_data/AdvancedTutorial/small_dataset.parquet")
print(df)
