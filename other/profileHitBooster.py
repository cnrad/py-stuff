# USAGE: `py profileHitBooster.py camo.githubusercontent.com/url-here`
# github will rate-limit camo usercontent occasionally. not built for efficiency lol just as an experiment

import requests
import threading
import time
import sys

hitUrl = sys.argv[1]
totalCount = 0

def do_request():
    r = requests.get(url=hitUrl)
    global totalCount 
    if 'Error Fetching Resource' in r.text:
        print('Rate Limited')
    else:
        totalCount += 1
        print("Hits added: %s" % totalCount)

def start_threads():
    while True:
        threads = []
        
        for i in range(90):
          t = threading.Thread(target=do_request)
          t.daemon = True
          threads.append(t)

        for i in range(90):
          threads[i].start()

        for i in range(90):
          threads[i].join()

        time.sleep(30)

start_threads()
