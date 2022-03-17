from faker import Faker
from kafka import KafkaProducer
import json
import time
import urllib
import requests
from datetime import date

fake = Faker()

def serializer(message):
    return json.dumps(message).encode('utf-8')

def get_registered_user():
    today = date.today()
    urls = urllib.parse.urlencode(
        {'query': '{job="Demo"} |= "login"','limit': '100'})

    s = requests.Session()
    r = s.get("http://localhost:3100/loki/api/v1/query",
            stream=True, params=urls)

    data = r.json()

    source_data = data['data']['result']

    ipaddress = []
    log_message = []
    fmt_time = []
    for i in source_data:
        values = i['values']
        for j in values:
            split_values = j[1].split("\t")
            ip = split_values[2]
            ipaddress.append(ip)
            message = split_values[3].replace("\r", "")
            log_message.append(message)
            fmt_time.append(str(today)+" "+split_values[1])
            #for a in range(len(ipaddress)):
            return {
                    'time': fmt_time[0],
                    'ip': ipaddress[0],
                    'message': log_message[0]
                }
       

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=serializer)


if __name__ =="__main__":
    while 1==1:
        producer.send('logs_stream', get_registered_user())
        print(get_registered_user())
        producer.flush()
        time.sleep(0.3)
