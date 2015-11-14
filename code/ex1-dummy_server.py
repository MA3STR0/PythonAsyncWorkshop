import time
from tornado.web import Application, RequestHandler
from tornado.gen import coroutine, Task
from tornado.ioloop import IOLoop


class DummyAPI(RequestHandler):
    @coroutine
    def get(self):
        yield Task(IOLoop.current().add_timeout, time.time() + 1)
        self.write('Hello, World!')
        self.finish()


if __name__ == "__main__":
    app = Application([(r"/", DummyAPI)])
    app.listen(8000)
    IOLoop.instance().start()
