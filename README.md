BETTER ASYNC CODE WITH PYTHON 3
===============================

#### Workshop on PyCon.Es, Valencia, 20.11.2015

_Contains training tasks for making http requests: 
first in blocking way, then async using AsyncIO, and finally async using Tornado._

- Task description follows below
- Example solutions are in the `code/` directory
- Feel free to extend, improve, send pull requests
- MIT-licence, everyone is free to reuse this workshop


#### REQUIREMENTS

- Python 3.4.1+
- aiohttp
- tornado
- pyvenv is a good idea


### EXERCISE 1

1. Write a dummy minimal 'greeting' web-app that waits for one second and sends a greeting (eg Hola, Pycon) to the browser.
Use any web-framework you like.


### EXERCISE 2

1. Write a script that requests greeting from ex1 on your local web-server and prints it to shell.
Use your favorite blocking http-library - requests, urllib, etc.
Request time should result in around 1 second.

2. Modify your code to call the greeting-server of your neighbour. Delay should be a bit more then 1 second.

3. Modify your code to get greetings of 3 neighbours in a loop.
Since requests are sequential, time would be more then 3 seconds.


### EXERCISE 3

1-3. Do same tasks like in Ex.2, but with AsyncIO + aiohttp library.


### EXERCISE 4

1-3. Do same tasks like in Ex.2, but with Tornado + tornado AsyncHTTPClient.


_Example solutions are in the `code/` directory._

_Initial tutor/author: [Anton](http://caceres.me)_
