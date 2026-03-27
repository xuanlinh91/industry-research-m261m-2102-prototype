import pandas as pd

INPUT_FILE = "HDFS_2k_cleaned.csv"
OUTPUT_FILE = "HDFS_2k_sequences.csv"

df = pd.read_csv(INPUT_FILE)
df = df[df["HasBlockId"] == True]
df = df.sort_values(by=["BlockId", "Timestamp"])

grouped = df.groupby("BlockId")["EventId"].apply(list).reset_index()
grouped.columns = ["BlockId", "EventSequence"]
grouped["SequenceLength"] = grouped["EventSequence"].apply(len)

grouped.to_csv(OUTPUT_FILE, index=False)
print(f"Saved {OUTPUT_FILE}")
print(grouped.head().to_string(index=False))
