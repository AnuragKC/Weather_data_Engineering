import json
from datetime import datetime
import requests  
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("weather")

def get_weather_data(city):  
    api_url = "http://api.weatherapi.com/v1/current.json"
    api_key = "8ea0b14b8ba94d5fb5d205945241312"  # Replace with your actual API key
    params = {  
        "q": city,    
        "key": api_key
    }  
    response = requests.get(api_url, params=params)  
    data = response.json()  
    return data  

def lambda_handler(event, context):
    cities = ["New York", "Chicago", "Baltimore", "Charlotte", "Richmond"]
    for city in cities:
        data = get_weather_data(city)  
    
        temp = data['current']['temp_c']
        wind_speed = data['current']['wind_mph']
        wind_dir = data['current']['wind_dir']
        pressure_mb = data['current']['pressure_mb']
        humidity = data['current']['humidity']
    
        print(city, temp, wind_speed, wind_dir, pressure_mb, humidity)
        current_timestamp = datetime.utcnow().isoformat()
        
        item = {
                'city': city,
                'time': str(current_timestamp),
                'temp': temp,
                'wind_speed': wind_speed,
                'wind_dir': wind_dir,
                'pressure_mb': pressure_mb,
                'humidity': humidity
            }
        item = json.loads(json.dumps(item), parse_float=Decimal)
        
        # Insert data into DynamoDB
        table.put_item(
            Item=item
        )