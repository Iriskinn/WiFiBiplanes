from __future__ import print_function
from gevent.pywsgi import WSGIServer
import json
import urllib
import threading
import time


IP_ADDR = '127.0.0.1'
MAIN_PORT = 8080
WEB_PORT = 8081