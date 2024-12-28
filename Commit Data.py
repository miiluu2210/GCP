#Import library needed
import pymssql
from google.cloud import storage
import csv
import pandas as pd


#Define function to authorize account by Service account key
def authorize_gcp(account_key):
    storage_client = storage.Client.from_service_account_json(account_key)
    return storage_client

#Define function to connect with data source:
def connect_source(**kwargs):
    conn = pymssql.connect(**kwargs)
    return conn

#Retrive data from query:
def retreive_data (connection, query):
    cursor = connection.cursor()
    data = cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Upload the CSV file to GCS
def upload_to_gcs(bucket_name, target_file_name, data, storage_client):
    # Generate the CSV content in memory
    temp_file = '/tmp/temp_data.csv'
    with open(temp_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    # Upload the CSV file to the specified GCS bucket
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(target_file_name)
    blob.upload_from_filename(temp_file)
    print(f"File {target_file_name} uploaded to bucket {bucket_name}.")




if __name__ == '__main__':
    # Authenticate
    storage_client = authorize_gcp('ancient-episode-383612-4a6f8ce04a9e.json')
    connection = connect_source(server = "45.117.83.230",
                                port = 1433,
                                user = "DA_72_Students",
                                password = "Student!1st",
                                database = "Ecommerce")
    table_name = "dispute_pp05"
    query = f"SELECT * FROM {table_name}"
    data = retreive_data(connection, query)
    df = pd.DataFrame(data)
    file_target = df.to_csv(f'data_{table_name}.csv')

    upload_to_gcs("paypal_transactions", table_name, file_target, storage_client )