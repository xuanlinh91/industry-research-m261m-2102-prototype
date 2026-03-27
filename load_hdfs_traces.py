import pandas as pd

traces = pd.read_csv("preprocessed/Event_traces.csv")
labels = pd.read_csv("preprocessed/anomaly_label.csv")

traces = traces.rename(columns={"Label": "TraceLabel"})
labels = labels.rename(columns={"Label": "AnomalyLabel"})

df = traces.merge(labels, on="BlockId", how="inner")

print("Merged columns:", df.columns.tolist())
print("Total sessions:", len(df))
print("Normal:", (df["AnomalyLabel"] == "Normal").sum())
print("Anomaly:", (df["AnomalyLabel"] == "Anomaly").sum())

df.to_csv("HDFS_v1_ready.csv", index=False)
print("Saved HDFS_v1_ready.csv")
