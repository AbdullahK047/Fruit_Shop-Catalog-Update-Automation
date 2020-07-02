#!/usr/bin/env python3

import os, glob
from PIL import Image

newsize = 600, 400

for file in glob.glob("supplier-data/images/*"):
  # print(file)
  try:
    im = Image.open(file).convert('RGB')
    im.resize((newsize)).save(file[:-5] + ".jpeg", "JPEG")
  except:
    pass
