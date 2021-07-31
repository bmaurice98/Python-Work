from os import device_encoding
import sys, getopt, fileinput
from typing import ChainMap

Encoded = ""

n = 8

splitEncoded = [Encoded[i : i + n] for i in range(0, len(Encoded), n)]
decoded = ""
for letter in splitEncoded:
    convertToInt = int(letter, 2)
    convertToChar = chr(convertToInt)
    decoded += convertToChar

print(decoded)
