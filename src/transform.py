import pandas as pd

def transform_data(df):
    try:
        df['order_date'] = pd.to_datetime(df['order_date'])
        df['revenue'] = df['total_price']
        print(f"Data transformed.")
        return df


    except Exception as e:
        print(f"Failed to transform data: {e}")
