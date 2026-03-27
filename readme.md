you can paste directly:

---

````markdown
## Team Setup & Usage Guide

This project uses the HDFS_v1 dataset for anomaly detection. Due to size limitations, the dataset is managed separately from the Git repository.

---

## 1. Project Setup

Clone the repository:

```bash
git clone <repo-url>
cd industry-research-m261m-2102-prototype
````

---

## 2. Dataset Setup (Required)

Download the processed dataset:

```
HDFS_v1_ready.csv
```

Download link:
[PASTE SHARED LINK HERE]

Place the file in the project root:

```
./HDFS_v1_ready.csv
```

---

## 3. Optional: Recreate Dataset from Raw Files

If needed, the dataset can be regenerated.

### Step 1: Download HDFS_v1 dataset

Download from:
[https://github.com/logpai/loghub](https://github.com/logpai/loghub)

Place files inside:

```
./preprocessed/
```

---

### Step 2: Run preprocessing script

```bash
python3 load_hdfs_traces.py
```

This will generate:

```
HDFS_v1_ready.csv
```

---

## 4. Pipeline Overview

The data pipeline consists of three stages:

### 1. Cleaning Raw Logs

```bash
python3 clean_hdfs.py
```

* Standardises timestamps
* Extracts BlockId (session key)
* Cleans log messages
* Preserves original logs for traceability

---

### 2. Sequence Construction (Sample Data)

```bash
python3 build_sequences.py
```

* Groups logs by BlockId
* Builds event sequences

---

### 3. Final Dataset Preparation

```bash
python3 load_hdfs_traces.py
```

* Loads Event_traces.csv and anomaly_label.csv
* Merges into final dataset
* Outputs HDFS_v1_ready.csv

---

## 5. Dataset Schema

The final dataset contains:

* BlockId → session identifier
* TraceLabel → Success / Fail
* Features → event-based feature vector
* TimeInterval → temporal behaviour vector
* Latency → numeric metric
* AnomalyLabel → Normal / Anomaly

---

## 6. Team Responsibilities

### ML / AI Team

* Use `HDFS_v1_ready.csv`
* Train anomaly detection models
* Evaluate using standard metrics

### Software Team

* Build API for predictions
* Map BlockId to original logs
* Develop frontend dashboard

---

## 7. Notes

* Do not commit large dataset files to Git
* Ensure dataset is placed in the correct path before running scripts
* Use the same dataset version across all team members

## HDFS Anomaly Detection Pipeline
                ┌──────────────────────────────┐
                │     Raw HDFS Logs (HDFS.log) │
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │   Data Cleaning & Parsing    │
                │                              │
                │ - Standardise timestamps     │
                │ - Extract BlockId            │
                │ - Clean log messages         │
                │ - Preserve original logs     │
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │     Structured Log Dataset   │
                │                              │
                │ LineId, Timestamp, Component │
                │ BlockId, EventId, Template   │
                │ Original + Cleaned Content   │
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │   Sequence Construction      │
                │                              │
                │ BlockId → [E1, E5, E8, ...]  │
                └──────────────┬───────────────┘
                               │
                               ▼
        ┌──────────────────────────────────────────────┐
        │        Preprocessed HDFS_v1 Dataset          │
        │                                              │
        │ Event_traces.csv + anomaly_label.csv         │
        └──────────────┬───────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────────────┐
        │        Final Modelling Dataset               │
        │          (HDFS_v1_ready.csv)                 │
        │                                              │
        │ BlockId, Features, TimeInterval, Latency     │
        │ AnomalyLabel                                │
        └──────────────┬───────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────────────┐
        │        Anomaly Detection Models              │
        │                                              │
        │ - Isolation Forest                          │
        │ - Autoencoder                              │
        │ - LSTM / DeepLog                           │
        └──────────────┬───────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────────────┐
        │          Prediction Output                   │
        │                                              │
        │ BlockId → Normal / Anomaly                  │
        │ Anomaly Score                              │
        └──────────────┬───────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────────────┐
        │         Traceability Layer                   │
        │                                              │
        │ BlockId → Original Logs                     │
        │ - Timestamp                                 │
        │ - Component                                 │
        │ - Source (IP)                               │
        └──────────────┬───────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────────────┐
        │        Frontend / Dashboard                  │
        │                                              │
        │ - Anomaly alerts                            │
        │ - Source identification                     │
        │ - Log trace view                            │
        │ - Timeline analysis                         │
        └──────────────────────────────────────────────┘