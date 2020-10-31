import webbrowser
import time 
import random

while True:
	sites = random.choice(['google.com', 'facebook.com', 'instagram.com'])
	visit = "http://{}".format(sites)
	webbrowser.open(visit)
	seconds = random.randrange(5, 20)
	time.sleep(seconds)