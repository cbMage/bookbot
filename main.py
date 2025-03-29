import sys

def main(path):
    from stats import reporter
    print(reporter(path))

if len(sys.argv)<2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
   
