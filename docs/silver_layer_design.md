# Silver Layer Design

## Purpose

Transform Bronze data into cleansed, business-ready datasets.

## Transformations Applied

### Orders

- Removed null order_id records
- Removed duplicate order_id records
- Standardized order_status values
- Created order_purchase_date
- Created delivery_days
- Created is_delivered_late flag

## Derived Columns

### order_purchase_date

Business date extracted from order_purchase_timestamp.

### delivery_days

Difference between customer delivery date and purchase date.

### is_delivered_late

1 = Delivered after estimated delivery date

0 = Delivered on time
