import asyncio
import aiohttp
import time

URLS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8000',
]

@asyncio.coroutine
def request_greetings():
    response_tasks = yield from asyncio.wait([aiohttp.get(url) for url in URLS])
    text_tasks = yield from asyncio.wait(
        [task.result().text() for task in response_tasks[0]]
    )
    texts = [task.result() for task in text_tasks[0]]
    return '\n'.join(texts)


loop = asyncio.get_event_loop()
t1 = time.time()
greetings = loop.run_until_complete(request_greetings())
print(time.time() - t1, 'seconds passed')
print(greetings)
loop.close()
