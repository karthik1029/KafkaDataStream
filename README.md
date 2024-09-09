# Kafka Weather Data Streaming to InfluxDB

A project that streams weather data from an external API to a Kafka topic, and then consumes that data to store it in an InfluxDB time series database.

## Features

- **Stream real-time weather data**: The script fetches weather data from the Open-Meteo API and streams it into Kafka, making it available for consumption by various services.
- **Store weather data in InfluxDB**: A Kafka consumer reads the weather data from Kafka and stores it in InfluxDB for efficient time series analysis and querying.

## Prerequisites

- Python 3.8+
- Kafka
- InfluxDB

## Installation

### Step 1: Install and Start Kafka

1. [Download and install Kafka](https://kafka.apache.org/downloads).
2. Start Zookeeper:
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
3. Start Kafka
   ```bash
   bin/kafka-server-start.sh config/server.properties
   
### Step 2: Install and Start InfluxDB

1. Download and install InfluxDB.
2. Start InfluxDB
   ```bash
   influxd

### Step 3: Configure Environment Variables

1. Set up a Python virtual environment and install dependencies
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install requests kafka-python influxdb-client
   
2. Create a .env file in the root directory and configure the following environment variables
   ```bash
   INFLUXDB_URL="http://localhost:8086"
   INFLUXDB_TOKEN="your-influxdb-token"
   INFLUXDB_ORG="your-org"
   INFLUXDB_BUCKET="weather_data_bucket"
   KAFKA_BOOTSTRAP_SERVERS="localhost:9092"


#### Step 5: Run the Kafka Producer and Consumer

1. Run the script that fetches weather data and sends it to Kafka:
   ```bash
   python kafka_weather_producer.py

2. Run the script that consumes weather data from Kafka and writes it to InfluxDB:
   ```bash
   python kafka_influxdb_consumer.py

#### Step 6: Accessing the Data
- Once the scripts are running, you can query the weather data stored in InfluxDB using the InfluxDB UI or CLI by navigating to http://localhost:8086/



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

### MIT License


