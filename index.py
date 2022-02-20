import os
import sys
from googletrans import Translator
import re

path=sys.argv[1]

translator=Translator()

def translating(filename):
  file = open( filename, "r")
  lines = file.readlines()
  file.close()

  for line in range(len(lines)):
    if re.search('^[0-9]+$', lines[line]) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', lines[line]) is None and re.search('^$', lines[line]) is None:
      lines[line]=translator.translate(lines[line],dest="fa").text

  file=open(filename,"w")
  for i in lines:
    file.write(i)
  file.close

for file in os.listdir(path):
    if file.endswith(".srt"):
        translating(os.path.join(path, file))
        print("\nsuccessful "+str(file))
print("\n-------------- done ------------\n")

