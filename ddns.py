import requests
import time

while True:
    requests.get('https://www.duckdns.org/update?domains=pi-srv-vpn&token=a134eaa3-ec04-4a1a-8930-01b018e118e4&ip=')
    time.sleep(300)