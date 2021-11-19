# USAGE: `py profileHitBooster.py camo.githubusercontent.com/url-here`
# github will rate-limit camo usercontent occasionally. not built for efficiency lol just as an experiment

import requests
import threading
import time
import sys

hitUrl = 'https://hits.link/hits?url=https://github.com/cnrad'
totalCount = 0

def do_request():
    r = requests.get(url=hitUrl)
    global totalCount 
    if 'Error Fetching Resource' in r.text:
        print('Rate Limited')
    else:
        totalCount += 1
        print("Hits added: %s" % totalCount)
        print(r.text)

def start_threads():
    while True:
        do_request()

        time.sleep(15)

start_threads()

    