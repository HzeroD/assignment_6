# ML Monitoring 

1. Process Monitoring
    - DAG, compute, endpoints, etc. 
    - networking, CPU, GPU, memory, disk, etc.
    - latencty, throughput, error rates, etc.

2. Data Monitoring
    - Drift - divergence between the data your model was trained on and the data it is currently seeing( at inference time).
        - Data Drift - there is a change in dist of data 
          - financial model - trained - data - income level is around 25k-75k 
            - deploy - if - data - income levels > 120k - !
        - Concept Drift - if there is a fundamental change in relationship between features and target
          - spam detection - train - 2016 data - 'crypto' -> spam
            - 2026 - 'crypto' is not spam 
  
## How to detect drift in prod

Statistical divergence measures. Compare the distribution of the training data with the distribution of the inference data ( last 10 mins, last 7 days, last few months ).

- PSI - Population Stability Index
  - divide the data into 10 buckets. PSI calculate the difference in data falling into each bucket between the training and inference data.
  - 
  - PSI < 0.1 - no significant drift
  - PSI 0.1 - 0.2 - moderate drift
  - PSI > 0.2 - significant drift

    - PSI = sum((% of inference data in bucket - % of training data in bucket) * ln(% of inference data in bucket / % of training data in bucket))

- KL Divergence - Kullback-Leibler Divergence
- Jensen-Shannon Divergence
- Wasserstein Distance