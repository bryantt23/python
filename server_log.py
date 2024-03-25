# Expected Tests to Pass
# Based on the provided log content, here are some tests your script should aim to pass:

# The most frequently visited URL should be /index.html.
# The count of 4XX status codes should be 2 (403 and 404).
# The count of 5XX status codes should be 2 (503 and 500).

import re


def start():
    print("hi")
    url_ct = {}
    with open("server_log.log") as f:
        for line in f:
            match = re.search(r'"(GET|POST) (.+?) HTTP', line)
            if match:
                url = match.group(2)
                if url in url_ct:
                    url_ct[url] += 1
                else:
                    url_ct[url] = 1

    most_frequent_url = max(url_ct, key=url_ct.get)
    get_request_cts = sum(url_ct.values())
    print(f"most freq: {most_frequent_url}")
    print(f"request ct: {get_request_cts}")


start()
