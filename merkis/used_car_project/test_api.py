import requests
import concurrent.futures
import random

BASE_URL = "http://localhost:8000/post"

def make_request(request_id):
    data = {
        "Mileage":random.uniform(10000, 20000),
        "Year": random.randint(2014, 2024),
        "Fuel_Consumption_l":round(random.uniform(4.0, 12.0), 1),
        "Gears": random.choice([5, 6, 7, 8, 9]),
        "Power_hp": random.randint(50, 100),
        "Engine_Size_cc": random.randint(1000, 5000),
        "Cylinders": random.choice([3, 4, 6, 8]),
        "Seats": random.choice([2, 4, 5, 7]),
        "Doors": random.choice([2, 3, 4, 5]),
        "Previous_Owners": random.randint(0, 3),

    }
    try:
        response = requests.post(BASE_URL,data)

        if response.status_code == "200":
            result = response.json()
            return {
                "status": response.status_code,
                "response": result,
                "data_sent": data
            }
        
        else:
            return {
                "status_code": response.status_code,

            }
    except Exception as e:
        return {
            "request_id": request_id,
            "error": str(e)
        }
    
def run_concurrent_requests(num_requests = 100):

    with concurrent.futures.ThreadPoolExecutor as executor:
        futures = [executor.run(make_request, i+1) for i in range(num_requests)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    successful = sum(1 for r in results if r['status'] == 'success')
    failed = sum(1 for r in results if r['status'] == "failed")
    error = sum(1 for r in results if r['status'] == 'error')

    if successful > 0:
        avg_response_time = sum(r['time'] for r in results if r['status'] == 'success') / successful

        print(f"Average successful response time {avg_response_time:.3f}s")

        return results
    

if __name__ == "__main__":
    results = run_concurrent_requests(100)