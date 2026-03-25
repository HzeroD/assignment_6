# Cloud

1. Compute
2. Storage
3. Managed Services - automate lifecycle of MLOps


## Provider 

1. AWS
   1. Compute - EC2 : 4vCPU, 16GB RAM / 16vCPU, 32GB RAM / 16vCPU, 32GB RAM, 2 x NVIDIA T4 GPU
   2. Storage - S3 - DBs: RDS, DynamoDB, Redshift
   3. Managed Services - SageMaker
2. Azure
   1. Compute - Azure VMs
   2. Storage - Azure Blob Storage - DBs: Azure SQL Database, Cosmos DB, Azure Synapse Analytics
   3. Managed Services - Azure Machine Learning
3. GCP
   1. Compute - Google Compute Engine
   2. Storage - Google Cloud Storage - DBs: Cloud SQL, Firestore, BigQuery
   3. Managed Services - Vertex AI


## MLOps

Automating - Lifecycle of Machine Learning Models.  


1. Automating Training - Use cloud services to schedule and run training jobs. Automate data pipeline, experiment tracking, and model versioning ( into the registry ), reporting ( metrics, logs, etc. ).

2. Deployment - Use cloud services to automate deployment of models into production. This includes setting up CI/CD pipelines, and managing model versions in production.

3. Tracking - Model and Data

4. Monitoring - Use cloud services to monitor the performance of models in production. This includes tracking metrics, detecting anomalies, and setting up alerts for model performance degradation.