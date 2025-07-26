# Data Product Simulation: Orders Pipeline with Metadata, Validation, and Lineage

## Overview

This project simulates a lightweight internal data product designed to process and deliver order-level data with built-in data governance, validation, and documentation. The pipeline reflects real-world data product design principles such as:

- Scalable data transformation
- Automated data quality checks
- Metadata extraction and schema transparency
- Basic data lineage tracking

The project is built entirely in Python and mimics aspects of platforms like **dbt**, **Collibra**, and governed **BI architecture**—similar to what I’ve led professionally in roles across analytics, product, and data strategy.

---

## 🔍 Business Use Case

A fictional e-commerce retailer needs a reliable data pipeline to analyze daily order activity. Key business requirements include:

- Accurate revenue calculations
- Validated input data to ensure operational KPIs are trustworthy
- Clear lineage from raw source to final analytic output
- Readable metadata for analysts and business users

This solution reduces ad hoc manual reporting, increases trust in self-service dashboards, and serves as the foundation for more advanced features (e.g., forecasting, anomaly detection, customer segmentation).

---

## Tech Stack

| Component              | Tool/Library         |
|------------------------|----------------------|
| Ingestion              | `pandas`             |
| Transformation         | `pandas`             |
| Data Validation        | `great_expectations` |
| Metadata Generation    | `pandas`, `json`     |
| Lineage Diagram        | `graphviz`           |
| Output Format          | CSV, PNG, Markdown   |

---

## Pipeline Flow

```text
Raw CSV (orders.csv)
   ↓
[Ingest] → [Transform] → [Validate] → [Generate Metadata] → [Export]
                                           ↓
                                    Lineage Diagram
