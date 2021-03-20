from datetime import date
import time
import requests
from plyer import notification

covid_data = None

try:
    covid_data = requests.get(
        "https://corona-rest-api.herokuapp.com/Api/bulgaria/")
except:
    print('Please, check your internet connection!')

print(covid_data)

if not covid_data == None:
    data = covid_data.json()['Success']

print(data)
#     while True:

#         notification.notify(
#             title=f'COVID-19 STATS ON {date.today()}',
#             message=f"Total cases: {data['cases']} Today cases: {data['todayCases']}",)
