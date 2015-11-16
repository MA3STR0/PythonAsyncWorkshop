from urllib.request import urlopen
import time

URLS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8000',
]

def request_greetings():
    responses = []
    for url in URLS:
        resp = urlopen(url)
        responses.append(resp.read().decode('utf-8'))
    texts = '\n'.join(responses)
    return texts


if __name__ == "__main__":
    t1 = time.time()
    greetings = request_greetings()
    print(time.time() - t1, "seconds passed")
    print(greetings)
