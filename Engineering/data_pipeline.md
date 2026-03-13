# Data Pipeline

## ETL

1. Extract
    - Extract data from various sources such as databases, APIs, or files.

2. Transform
    - Clean and preprocess the data, including handling missing values, normalizing data, and performing feature engineering.

3. Load
    - Load the transformed data into a target database for analysis and reporting.


## Why does MLE need data pipeline?

- Training - Inference Consistency: A data pipeline ensures that the same data preprocessing steps are applied during both training and inference.

- Memory Limits : the data pipeline being a different process from the training process, allow us use data pipeline techniques. 


## Airflow 

- acts like an orchestrator.
- you write DAG - Directed Acyclic Graph.
- Directed: it flow in only one direction.
- Acyclic: it doesn't have cycles, meaning that you can't go back to a previous
- Graph: network of interconnected tasks.