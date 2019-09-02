#! /usr/bin/env python3
import os
import re
import sys

def main():
    # setting cmdLine arguments for file names
    textFile = sys.argv[1]
    outputFile = sys.argv[2]

    # parse input file
    readText = open(textFile).read()
    wordList = readText.lower().split()
    wordSet = set(wordList)
    # sorted(wordSet)
    # print(sorted(wordSet))

    createOutputFile(outputFile)

    # exclude punctuation and whitespace
    for w in wordSet:
        w = re.sub(r"[^a-z0-9]","", w)
        print(w, ": ", wordList.count(w))

        with open(outputFile, "a") as f:
            f.write("%s: %d\n" % (w, wordList.count(w)))
            f.close()

# create output file
def createOutputFile(outputFile):
    if not os.path.exists(outputFile):
        with open(outputFile, 'w'): pass

main()