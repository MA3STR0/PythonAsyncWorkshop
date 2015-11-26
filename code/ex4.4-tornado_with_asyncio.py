from tornado.platform.asyncio import AsyncIOMainLoop, to_asyncio_future
from tornado.httpclient import AsyncHTTPClient
import asyncio
import time


URL = 'http://127.0.0.1:8000'


@asyncio.coroutine
def get_greetings():
    http_client = AsyncHTTPClient()
    response = yield from to_asyncio_future(http_client.fetch(URL))
    return response.body.decode('utf-8')


if __name__ == "__main__":
    AsyncIOMainLoop().install()
    loop = asyncio.get_event_loop()
    t1 = time.time()
    texts = loop.run_until_complete(get_greetings())
    print(time.time() - t1, "seconds passed")
    print(texts)
    loop.close()
