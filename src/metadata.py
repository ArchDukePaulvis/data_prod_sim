import json
import os
import pandas as pd
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (pd.Timestamp, pd.Timedelta, np.integer, np.floating, np.ndarray)):
            return str(obj)
        return super().default(obj)
    
def generate_metadata(df, output_dir):
    try:
         
        os.makedirs(output_dir, exist_ok=True)
        
        metadata = {
            'columns': {col: str(dtype) for col, dtype in df.dtypes.items()},
            'row_count': len(df),
            'sample_data': df.head(3).to_dict(orient='records')
        }
        
        # Save JSON metadata to outputs/metadata
        json_path = os.path.join(output_dir, "metadata.json")
        with open(json_path, "w") as f_json:
            json.dump(metadata, f_json, indent=4, cls=NpEncoder)

        # Save human-readable Markdown catalog to outputs/metadata
        md_path = os.path.join(output_dir, "data_catalog.md")
        with open(md_path, "w") as f_md:
            f_md.write("Data Catalog\n\n")
            f_md.write(f"**Total Rows:** {metadata['row_count']}\n\n")
            f_md.write("**Columns:**\n\n")
            f_md.write("| Column Name | Data Type |\n")
            f_md.write("|-------------|-----------|\n")
            for col, dtype in metadata["columns"].items():
                f_md.write(f"| {col} | {dtype} |\n")

        print(f"Metadata saved.")

    except Exception as e:
        print(f"Failed to generate metadata: {e}")