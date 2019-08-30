#! /usr/bin/env python3
import sys
import os

# setting cmdLine arguments for file names
textFile = sys.argv[1]
inputFile = sys.argv[2]
outputFile = sys.argv[3]

if not os.path.exists(outputFile):
    with open('outputFile', 'w'): pass


