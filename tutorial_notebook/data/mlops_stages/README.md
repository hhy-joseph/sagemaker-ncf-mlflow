# Data Split for MLOps Stages

## Overview
This data has been split to simulate a real-world MLOps scenario:
- **Historical data (90%)**: Used for initial model development (Stage 1)
- **Future data (10%)**: Represents "unseen" future data for MLOps training (Stages 2-3)

## Split Information
- Original dataset: 892 trading days
- Historical data: 802 trading days (89.9%)
  - Date range: 2021-06-16 00:00:00+00:00 to 2024-08-22 00:00:00+00:00
- Future data: 90 trading days (10.1%)
  - Date range: 2024-08-23 00:00:00+00:00 to 2024-12-31 00:00:00+00:00

## Usage Guidelines
1. **Stage 1**: Use only historical_features.csv
2. **Stage 2**: Use historical_features.csv for training, simulate "new" data arriving with future_features.csv
3. **Stage 3**: Implement production pipeline using historical_features.csv, then validate using future_features.csv

## Important Notes
- Do not use future data for initial model training
- Feature engineering should be consistent across both datasets
- Use the future data to simulate real-world model performance evaluation

Created on: 2025-02-19
