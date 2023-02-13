import random
from time import sleep

def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration