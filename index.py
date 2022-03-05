import os
import sys
from googletrans import Translator
import re
from tqdm import tqdm
import time

path=sys.argv[1]

translator=Translator()

def translating(filename):
  file = open( filename, "r")
  lines = file.readlines()
  file.close()

  for line in tqdm(range(len(lines)),colour="green"):
    if re.search('^[0-9]+$', lines[line]) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', lines[line]) is None and re.search('^$', lines[line]) is None:
      time.sleep(0.1)
      lines[line]=translator.translate(lines[line],dest="fa").text

  file=open(filename,"w")
  for i in lines:
    file.write(i)
  file.close

if(path.endswith(".srt")):
    try:
      translating(path)
      print("\nsuccessful "+str(path))
    except:
      print("not translateing !")
else:
    for file in os.listdir(path):
      if file.endswith(".srt"):
        try:
          translating(os.path.join(path, file))
          print("\nsuccessful "+str(file))
        except:
          continue

print("\n-------------- done ------------\n")

