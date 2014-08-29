import os
import socket
import sys

TMP_DIR = '/tmp/pymq'

if not os.path.exists(TMP_DIR):
	os.makedirs(TMP_DIR)

VERSION = sys.version_info[0]

HOST = ''
MAX_CLIENTS = 10
PORT = 8080
