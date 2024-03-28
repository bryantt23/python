import os
import sys


def test():
    print('hi')
    pass


test()


# This block allows the script to be called with arguments from the command line
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: mygrep.py [query] [path]")
    else:
        query = sys.argv[1]
        path = sys.argv[2]
        results = mygrep(query, path)
        for result in results:
            print(result)
