import socket

from pymq.settings import PORT as PORT
from pymq.settings import MAX_CLIENTS as MAX_CLIENTS

class MessageServer(object):
	def __init__(self, *args, **kwargs):
		self._socket = None
		self.__dict__.update(kwargs)
		super(MessageServer, self).__init__()

	def start(self):
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.bind((socket.gethostname(), PORT))
		self._socket.listen(MAX_CLIENTS)

	def stop(self):
		if(not self._socket):
			return
		self._socket.shutdown(0)
		self._socket.close()
