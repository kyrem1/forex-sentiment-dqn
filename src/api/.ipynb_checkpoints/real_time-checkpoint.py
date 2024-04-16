import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import matplotlib.dates as mdates

with open('api_access.txt', 'r') as file:
    lines = file.readlines()
token = lines[0].strip()
account_id = lines[1].strip()

headers = {
    'auth-token': token
}
url = f'https://mt-client-api-v1.new-york.agiliumtrade.ai/users/current/accounts/{account_id}/symbols/EURUSD/current-tick'

times = []
asks = []
bids = []

def fetch_data():
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def update(frame_number):
    data = fetch_data()
    times.append(data['time'])
    asks.append(data['ask'])
    bids.append(data['bid'])

    if len(times) > 50:
        times.pop(0)
        asks.pop(0)
        bids.pop(0)

    plt.cla()  
    plt.plot(times, asks, label='Ask')
    plt.plot(times, bids, label='Bid')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Real-time Forex Data')
    plt.legend()
    plt.xticks(rotation=45)

fig = plt.figure()
ani = FuncAnimation(fig, update, interval=1000, save_count=50)

plt.tight_layout()
plt.show() 


