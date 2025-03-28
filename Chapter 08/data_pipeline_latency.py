import time
import boto3
import json
from snowflake.connector import connect

# Configuration
s3_bucket_name = "input_data_bucket"
s3_key = "sample_data.json"
sample_data = {
    "id": "sample_data_123",
    "name": "Latency Test",
    "timestamp": time.time(),
}
ingestion_time_column = "ingestion_time"
snowflake_table = "your_table"

# Assume the Snowflake connection is established
snowflake_conn = connect(
    user="your_user",
    password="your_password",
    account="your_account",
    database="your_database",
    schema="your_schema",
)


def upload_to_s3(bucket_name, key, data):
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data))
    print("Sample data uploaded to S3.")


def check_data_in_snowflake(conn, data_id, timeout=60):
    query = (
        f"SELECT {ingestion_time_column} FROM {snowflake_table} WHERE id = '{data_id}'"
    )

    start_time = time.time()
    while time.time() - start_time < timeout:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                ingestion_time = result[0]
                print("Data found in Snowflake.")
                return ingestion_time
        time.sleep(1)  # Wait for 1 second before querying again

    print("Data not found in Snowflake within the timeout period.")
    return None


def measure_latency(bucket_name, key, data, conn):
    start_time = time.time()
    upload_to_s3(bucket_name, key, data)
    ingestion_time = check_data_in_snowflake(conn, data["id"])
    if ingestion_time:
        latency = ingestion_time - data["timestamp"]
        print(f"Latency: {latency} seconds")
    else:
        print("Failed to measure latency.")


# Execute the latency measurement
measure_latency(s3_bucket_name, s3_key, sample_data, snowflake_conn)
