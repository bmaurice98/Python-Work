import sys, getopt
from pathlib import Path
from ast import literal_eval

inputfile = sys.argv[1:]

try:
    opts, argv = getopt.getopt(inputfile, "hi:", ["help", "inputfile="])

    for opt, arg in opts:

        if opt in ("-h", "--help"):
            print("UnicodeDecoder.py -i <inputfile>")
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            inputfile = arg

except getopt.GetoptError:
    print("UnicodeDecoder.py -i <inputfile>")
    sys.exit(2)


with open(inputfile, "r", encoding="utf-8") as f_open:
    unicode = f_open.read()
    string = eval(repr(unicode).replace("\\\\", "\\"))
    print(string)
