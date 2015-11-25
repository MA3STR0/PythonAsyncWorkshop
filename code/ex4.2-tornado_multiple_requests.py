from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import coroutine
import time


URLS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8000',
]


@coroutine
def get_greetings():
    http_client = AsyncHTTPClient()
    responses = yield [http_client.fetch(url) for url in URLS]
    texts = [resp.body.decode('utf8') for resp in responses]
    return '\n'.join(texts)


if __name__ == "__main__":
    loop = IOLoop.instance()
    t1 = time.time()
    text = loop.run_sync(get_greetings)
    print(time.time() - t1, "seconds passed")
    print(text)
