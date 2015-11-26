from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import coroutine
import time


URLS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8000',
]


class GreetingHandler(RequestHandler):
    @coroutine
    def get(self):
        t1 = time.time()
        http_client = AsyncHTTPClient()
        responses = yield [http_client.fetch(url) for url in URLS]
        texts = [resp.body.decode('utf8') for resp in responses]
        self.set_header('Content-Type', 'text/plain; charset=UTF-8')
        self.write('%s seconds passed\n' % (time.time() - t1))
        self.write('\n'.join(texts))
        self.finish()


if __name__ == "__main__":
    application = Application([
        (r"/", GreetingHandler),
    ])
    application.listen(8002)
    IOLoop.instance().start()
