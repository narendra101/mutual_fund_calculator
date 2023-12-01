import requests
from datetime import datetime
from fastapi import FastAPI

class MutualFundCalculator:
    def __init__(self):
        self.base_url = "https://api.mfapi.in/mf/"

    def get_nav(self, scheme_code, date):
        url = f"{self.base_url}{scheme_code}?date={date}"
        response = requests.get(url)
        nav_data = response.json().get("data")

        for d in nav_data:
            if d.get("date") == date:
                return d.get("nav")

        return nav_data.get("nav") if nav_data else None

    def calculate_profit(self, scheme_code, start_date, end_date, capital=1000000.0):
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        start_nav = self.get_nav(scheme_code, start_date.strftime("%d-%m-%Y"))
        end_nav = self.get_nav(scheme_code, end_date.strftime("%d-%m-%Y"))
        start_nav = float(start_nav)
        end_nav = float(end_nav)
        units_allotted = capital / start_nav
        value_on_redemption = units_allotted * end_nav
        net_profit = value_on_redemption - capital
        return round(net_profit, 2)

app = FastAPI()
calculator = MutualFundCalculator()

@app.get("/profit")
def calculate_profit(    
    scheme_code: str,
    start_date: str,
    end_date: str,
    capital: float
):
    profit = calculator.calculate_profit(scheme_code, start_date, end_date, capital)
    return {"net_profit": profit}
