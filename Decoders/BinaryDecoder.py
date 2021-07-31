from os import device_encoding, name
import sys, getopt
from typing import ChainMap
from pathlib import Path


inputfile = sys.argv[1:]

try:
    # Parsing arguments
    opts, argv = getopt.getopt(inputfile, "hi:", ["help", "inputfile="])

    # Check the arguments
    for opt, arg in opts:

        if opt in ("-h", "--help"):
            print("BinaryDecoder.py -i <inputfile>")
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            inputfile = arg

except getopt.GetoptError:
    print("BinaryDecoder.py -i <inputfile>")
    sys.exit(2)

# Reading in the input file
Encoded = Path(inputfile).read_text()
n = 8
# Splitting the bits apart, 8 at a time
splitEncoded = [Encoded[i : i + n] for i in range(0, len(Encoded), n)]
decoded = ""
for letter in splitEncoded:
    convertToInt = int(letter, 2)
    convertToChar = chr(convertToInt)
    decoded += convertToChar

print(decoded)
