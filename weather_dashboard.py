import requests
import matplotlib.pyplot as plt
import seaborn as sns


API_KEY = '9a15bbf119a2b0f62ab958414e21da5f'
CITY = 'Chennai'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    
    dates = []
    temps = []

    for forecast in data['list']:
        dates.append(forecast['dt_txt'])
        temps.append(forecast['main']['temp'])
    
    sns.set(style="darkgrid")
    
    plt.figure(figsize=(12,6))
    sns.lineplot(x=dates, y=temps, marker='o', color='orange')
    plt.xticks(rotation=45)
    plt.title(f"5-Day Temperature Forecast for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.show()

else:
    print("Error fetching data:", response.status_code)
