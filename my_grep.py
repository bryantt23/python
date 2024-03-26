import sys
import os


def mygrep(query, path):
    arr = os.walk(path)
    res = []
    for root, dirs, files in arr:
        for file in files:
            path = os.path.join(root, file)

            with open(path) as f:
                line_num = 1
                for line in f:
                    if query in line:
                        res.append(f"{os.path.normpath(path)}:{
                                   line_num}\t{line.strip()}")
                    line_num += 1

    # print(arr)
    # for file in os.listdir(query)
    return res


def fake_test_mygrep():
    tests = [
        ("exceedingly", "./stories", [
            os.path.normpath("./stories/a-dark-brown-dog.txt") +
            ":1\tTheir casual approach often exasperated them exceedingly. They used to gain a ...",
            os.path.normpath("./stories/1908/jack-london/to-build-a-fire.txt") +
            ":1\tDay had broken cold and grey, exceedingly cold and grey, when the man turned ..."
        ]),
        ("never", "./stories/poe", [
            os.path.normpath("./stories/poe/the-tell-tale-heart.txt") +
            ":3\tit. Whenever it fell upon me, my blood ran cold; and so by degrees--very..."
        ]),
        ("former", "./stories", []),
        ("exceedingly", "./stories/poe", []),
        ("casual approach often", "./stories",
         [os.path.normpath('stories\\a-dark-brown-dog.txt')+':1\tTheir casual approach often exasperated them exceedingly. They used to gain a ...']),
        ("very", "./stories", [
            os.path.normpath("./stories/poe/the-tell-tale-heart.txt") +
            ":1\tTrue! --nervous --very, very dreadfully nervous I had been and am; but why will you say that I am mad?...",
            os.path.normpath("./stories/poe/the-tell-tale-heart.txt") +
            ":3\tit. Whenever it fell upon me, my blood ran cold; and so by degrees--very...",
        ]),
    ]

    for query, path, expected in tests:
        print(f"\nTesting query: '{query}' in path: '{path}'")
        # Ensure this calls your script/function correctly
        result = mygrep(query, path)
        if sorted(result) == sorted(expected):
            print("✓ Test passed.")
        else:
            print("✗ Test failed.")
            print("  Expected:", expected)
            print("  Got:", result)

# Replace `mygrep(query, path)` with the actual call to your mygrep function/script,
# and ensure it returns the results in the expected format for comparison.


# fake_test_mygrep()

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
