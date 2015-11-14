from urllib.request import urlopen


def request_greeting():
    resp = urlopen('http://127.0.0.1:8000')
    text = resp.read()
    print(text)


if __name__ == "__main__":
    request_greeting()
