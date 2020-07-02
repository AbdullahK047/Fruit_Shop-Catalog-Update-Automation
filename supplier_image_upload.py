#!/usr/bin/env python3
import requests
import os

# This  uploads images to our web server using
# The Python Requests module

url = "http://localhost/upload/"
files = os.listdir("supplier-data/images")

for file in files:
  if file[-4:] == "jpeg":
    with open('supplier-data/images/' + file, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
