import sys, getopt
from pathlib import Path

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


Unicode = Path(inputfile).read_text()
letter = Unicode.encode("ascii", "ignore")

print(letter)
