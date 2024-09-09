import requests
from kafka import KafkaProducer
import json
import time

API_URL = "https://api.open-meteo.com/v1/forecast"
LOCATION = {'latitude': 52.52, 'longitude': 13.41}  #  Berlin
PARAMS = {
    'current': 'temperature_2m,wind_speed_10m',
    'hourly': 'temperature_2m,relative_humidity_2m,wind_speed_10m'
}

KAFKA_TOPIC = 'weather_data'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_weather_data():
    try:
        response = requests.get(API_URL, params={**LOCATION, **PARAMS})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def stream_to_kafka():
    while True:
        data = get_weather_data()
        if data:
            current_data = data.get('current', {})
            print(f"Sending data to Kafka: {current_data}")
            producer.send(KAFKA_TOPIC, value=current_data)
        time.sleep(10)  # Fetch and send data every hour/10 seconds

if __name__ == "__main__":
    try:
        stream_to_kafka()
    except KeyboardInterrupt:
        print("Stopping stream.")
    finally:
        producer.close()
