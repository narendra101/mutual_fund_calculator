# mutual_fund_api_caller.py
import requests

def calculate_mutual_fund_profit(scheme_code, start_date, end_date, capital):
    api_url = f"http://127.0.0.1:8000/profit?scheme_code={scheme_code}&start_date={start_date}&end_date={end_date}&capital={capital}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        result = response.json()
        net_profit = result.get("net_profit")
        print(f"Net Profit: {net_profit}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")

if __name__ == "__main__":
    scheme_code = "101206"
    start_date = "26-07-2023"
    end_date = "18-10-2023"
    capital = 1000000.0

    calculate_mutual_fund_profit(scheme_code, start_date, end_date, capital)
