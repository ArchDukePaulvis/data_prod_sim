from src import ingest, transform, validate, metadata, lineage

df = ingest.load_data('data/raw/orders.csv')
dft = transform.transform_data(df)
valid = validate.validate(dft)
meta = metadata.generate_metadata(dft, 'outputs')
lineage.generate_lineage('outputs/lineage_diagram')

# Save transformed data and metadata
dft.to_csv('data/processed/cleaned_orders.csv', index=False)
