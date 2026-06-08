import pandas as pd
import os

df = pd.read_csv("/opt/airflow/data/raw/asteroids_raw.csv")

print("Antes:", len(df))

df = df.dropna()

df["absolute_magnitude_h"] = pd.to_numeric(
    df["absolute_magnitude_h"],
    errors="coerce"
)

df["name"] = df["name"].astype(str).str.strip()

df["is_potentially_hazardous"] = (
    df["is_potentially_hazardous"]
    .astype(str)
)

df = df.dropna()

print("Depois:", len(df))

os.makedirs("/opt/airflow/data/processed", exist_ok=True)

df.to_csv(
    "/opt/airflow/data/processed/asteroids_processed.csv",
    index=False
)

print("Arquivo processado criado!")