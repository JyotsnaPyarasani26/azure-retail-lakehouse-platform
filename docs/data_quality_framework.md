# Data Quality Framework

## Objective

Validate Bronze layer datasets before Silver transformations.

## Quality Checks

### Null Primary Key Validation

- order_id
- customer_id
- product_id
- seller_id
- review_id

### Duplicate Primary Key Validation

Duplicate detection performed on business primary keys.

### Quality Metrics

Metrics stored in:

data_quality_audit

Columns:

- table_name
- total_rows
- null_primary_keys
- duplicate_primary_keys

## Findings

### bronze_reviews

- 1 null review_id
- 955 duplicate review_id values

Further business investigation required before Silver transformation.
