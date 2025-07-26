import pandas as pd

def load_data(file_path):
    try:
        print(f"File ingested.")
        return pd.read_csv(file_path)

    except Exception as e:
        print(f"Failed to ingest file: {e}")
