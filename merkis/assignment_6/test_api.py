import requests
import concurrent.futures
import numpy as np
import random

URL = "http://127.0.0.1:8000/predict"

def generate_sample_data():
        return {
                "tenure": random.randint(0,72),
                "MonthlyCharges": round(random.uniform(18.25, 118.75), 2),
                "TotalCharges": round(random.uniform(0.0, 8684.8), 2),
                "gender": random.choice(["Male", "Female"]),
                "Partner": random.choice(["Yes", "No"]),
                "Dependents": random.choice(["Yes", "No"]),
                "PhoneService": random.choice(["Yes", "No"]),
                "MultipleLines": random.choice(['No phone service', 'No', 'Yes']),
                "InternetService": random.choice(['No phone service', 'No', 'Yes']),
                "OnlineSecurity": random.choice(['No phone service', 'No', 'Yes']),
                "OnlineBackup": random.choice(['Yes', 'No', 'No internet service']),
                "DeviceProtection": random.choice(['No', 'Yes', 'No internet service']),
                "TechSupport": random.choice(['No', 'Yes', 'No internet service']),
                "StreamingTV": random.choice(['No', 'Yes', 'No internet service']),
                "StreamingMovies": random.choice(['No', 'Yes', 'No internet service']),
                "Contract": random.choice(['Month-to-month', 'One year', 'Two year']),
                "PaperlessBilling": random.choice(["Yes", "No"]),
                "PaymentMethod": random.choice(['Electronic check', 'Mailed check','Bank transfer (automatic)','Credit card (automatic)']),
            }


def make_request(request_id, data=None, URL=URL):
    if data == None:
        data = generate_sample_data()

    try:
        response = requests.post(URL, json=data)
        result = response.json()
        if response.status_code == 200:
            return {
                "request_id": request_id,
                "status": "success",
                "response": result,
                "data_sent": data
            }
        
        else:
            return {
                "request_id": request_id,
                "status": "failed",
                "status_code": response.status_code
            }
    
    except Exception as e:
        print(f"Request {request_id}: ERROR -- {e}")
        
        return {
            "request_id": request_id,
            "status": "error",
            "error": e
        }
    

def run_concurrent_requests(num_requests=100):

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:

        futures = [executor.submit(make_request, i+1) for i in range(num_requests)]

        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    success = sum(1 for r in results if r['status'] == 'success')
    failed = sum(1 for r in results if r['status'] == 'failed')
    error = sum(1 for r in results if r['status'] == 'error')

    print(f"Total requests: {num_requests}")
    print(f"Successful: {success}")
    print(f"Failed: {failed}")
    print(f"Error: {error}")

    return results

def batch_post(n_customers=50):
    batch_lst = []
    for i in range(n_customers):
        batch_lst.append(generate_sample_data())

    response = requests.post("http://127.0.0.1:8000/predict_batch", json=batch_lst)
    return response.json()


if __name__ == "__main__":
    # results = run_concurrent_requests(10)
    # print(results[7])
    print(batch_post())
