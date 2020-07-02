#! /usr/bin/env python3

import os
import requests
import json

dict_keys = ["name", "weight", "description", "image_name"]
all_details = []
files = os.listdir("supplier-data/descriptions/")
for file in files:
  i = 0
  details = {}
  file1 = open("supplier-data/descriptions/" + file, 'r')
  lines = file1.readlines()
  for line in lines:
    details[dict_keys[i]] = line.strip()
    i += 1
  details["image_name"] = file[:-3] + "jpeg"
  details["weight"] = details["weight"].split()[0]
#  print(details)
  all_details.append(details)
  response = requests.post("http://34.71.174.67/fruits/", json=details)

def get_all_details():
  return all_details