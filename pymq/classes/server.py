import select
import socket

from pymq.settings import PORT as PORT
from pymq.settings import MAX_CLIENTS as MAX_CLIENTS

class MessageServer(object):
	SERVER = 0
	CLIENT = 1
	def __init__(self, *args, **kwargs):
		self.type = MessageServer.SERVER
		self.timer = 0
		self._socket = None
		self.__dict__.update(kwargs)
		super(MessageServer, self).__init__()

	def start(self, timer = 0):
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.bind((socket.gethostname(), PORT))
		self._socket.listen(MAX_CLIENTS)
		self.timer = timer
		self.accept()

	# non-blocking accept
	#	cf. http://bit.ly/1orQCxV
	def accept(self):
		if(not self._socket):
			return
		while(self.timer):
			r, w, e = select.select([ self._socket ], [], [], 1)
			self.timer -= 1

	def stop(self):
		if(not self._socket):
			return
		self.timer = 0
		self._socket.shutdown(0)
		self._socket.close()
