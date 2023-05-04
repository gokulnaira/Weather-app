import requests
API_key="7d75cb76bfb268084353ca829e6087dd"
def get_data(place,days=None):
    url="http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_values=8*forecast_days    
    filtered_data=filtered_data[:nr_values]
    return filtered_data
