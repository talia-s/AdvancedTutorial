import polars as pl

complete_df = pl.read_parquet(
    "/fast_scratch_1/TRISEP_data/AdvancedTutorial/small_dataset.parquet"
)

# shuffle first
complete_df_shuffled = complete_df.sample(fraction=1.0, shuffle=True)

# Example: Take the first 10000 events
train_df = complete_df_shuffled.slice(offset=0, length=80000)
train_df.write_parquet("/home/talias/trisep2025/AdvancedTutorial/code/data/train_df.parquet")
test_df = complete_df_shuffled.slice(offset=80000, length=10000)
test_df.write_parquet("/home/talias/trisep2025/AdvancedTutorial/code/data/test_df.parquet")
validate_df = complete_df_shuffled.slice(offset=90000, length=10000)
validate_df.write_parquet("/home/talias/trisep2025/AdvancedTutorial/code/data/validate_df.parquet")
