from faker import Faker
from kafka import KafkaProducer
import json
import time
import urllib
import requests
from datetime import date


today = date.today()
urls = urllib.parse.urlencode(
    {'query': '{job="windows"}'})

s = requests.Session()
r = s.get("http://127.0.0.1:3100/loki/api/v1/query",
          stream=True, params=urls)

data = r.json()

print(data)
        
