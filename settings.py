from __future__ import print_function
from gevent.pywsgi import WSGIServer
import json
import urllib
import threading


IP_ADDR = '192.168.137.1'
MAIN_PORT = 8080
WEB_PORT = 8081