#! /usr/bin/env python3
import sys
import os
import re

# setting cmdLine arguments for file names
textFile = sys.argv[1]
outputFile = sys.argv[2]

readText = open(textFile).read()

wordList = readText.split()
wordSet = set(wordList)

# create output file
if not os.path.exists(outputFile):
    with open(outputFile, 'w'): pass

for w in wordSet:
    w = re.sub(r"[^a-z0-9]","", w.lower())

    print(w, ": ", wordList.count(w))

