from kafka import KafkaProducer
from soupsieve import select
from sqlalchemy import create_engine
import psycopg2
import json
import time
import pandas as pd

def serializer(message):
    return json.dumps(message).encode('utf-8')
i=0
def get_data():
    conn_string  = 'postgres://postgres:1999@localhost:5432/airflow'
    db = create_engine(conn_string)
    conn = db.connect()
    logs = "SELECT * FROM symbol_list"
    df = pd.read_sql(logs, conn)
    
    return df.iloc[len(df)-1]['symbol']

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=serializer)
if __name__ == "__main__":
    while 1==1:
        data = get_data()
        producer.send('fromdb', data)
        print(data)
        time.sleep(1)
