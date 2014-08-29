import os
import sys

TMP_DIR = '/tmp/pymq'

if not os.path.exists(TMP_DIR):
	os.makedirs(TMP_DIR)

VERSION = sys.version_info[0]

PORT = 5555
MAX_CLIENTS = 10
