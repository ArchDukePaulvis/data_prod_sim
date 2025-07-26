import great_expectations as ge

def validate(df):
    try:
        ge_df = ge.from_pandas(df)
        result = ge_df.expect_column_values_to_not_be_null('order_id')
        print(f"Data validated.")
        return result.success


    except Exception as e:
        print(f"Failed to validate data: {e}")