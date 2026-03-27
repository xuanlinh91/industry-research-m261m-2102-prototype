import re
import pandas as pd

INPUT_FILE = "HDFS_2k.log_structured.csv"
OUTPUT_FILE = "HDFS_2k_cleaned.csv"

df = pd.read_csv(INPUT_FILE)

for col in ["Level", "Component", "Content", "EventId", "EventTemplate"]:
    df[col] = df[col].astype(str).str.strip()

df["Date"] = df["Date"].astype(str).str.zfill(6)
df["Time"] = df["Time"].astype(str).str.zfill(6)

df["Timestamp"] = pd.to_datetime(
    df["Date"] + df["Time"],
    format="%m%d%y%H%M%S",
    errors="coerce"
)

df["BlockId"] = df["Content"].str.extract(r"(blk_-?\d+)", expand=False)
df["OriginalContent"] = df["Content"]

def clean_content(text):
    if pd.isna(text):
        return text
    text = str(text)
    text = re.sub(r"blk_-?\d+", "<BLOCK>", text)
    text = re.sub(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", "<IP>", text)
    text = re.sub(r"\b\d+\b", "<NUM>", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["CleanedContent"] = df["Content"].apply(clean_content)
df["HasBlockId"] = df["BlockId"].notna()

output_cols = [
    "LineId", "Date", "Time", "Timestamp", "Pid", "Level", "Component",
    "BlockId", "HasBlockId", "EventId", "EventTemplate",
    "OriginalContent", "CleanedContent"
]

df[output_cols].to_csv(OUTPUT_FILE, index=False)
print(f"Saved {OUTPUT_FILE}")
