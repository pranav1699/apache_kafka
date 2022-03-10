import json
from kafka import KafkaConsumer
from numpy import source
import psycopg2
hostname = 'localhost'
database = 'airflow'
username = 'postgres'
pwd = '1999'
port_id = 5432





if __name__ == '__main__':
    # Kafka Consumer
    consumer = KafkaConsumer(
        'logs_stream',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    for message in consumer:
        data = json.loads(message.value)
        data1 = list(data.values())
        time = data1[0]
        ip = data1[1]
        message = data1[2]

        
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id,
        )
        
        cur = conn.cursor()

        cur.execute(
            "CREATE TABLE IF NOT EXISTS stream_data (time varchar,ip varchar,message varchar);")
        i = 0

        insert_data = 'INSERT INTO stream_data (time,ip,message) VALUES(%s,%s,%s);'
        data = [time, ip, message]
        cur.execute(insert_data,data)

        #cur.execute(f'SELECT * FROM {tablename}')
        print(time, ip, message)
        conn.commit()

        cur.close()

        conn.close()
