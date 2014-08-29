import select
import socket

from pymq.settings import PORT as PORT
from pymq.settings import MAX_CLIENTS as MAX_CLIENTS

class MessageServer(object):
	def __init__(self, *args, **kwargs):
		self.__dict__.update(kwargs)
		self.clients = []
		self.timer = 0
		self._socket = None
		super(MessageServer, self).__init__()

	def start(self, timer = 0):
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.clients.append(self._socket)
		self._socket.bind((socket.gethostname(), PORT))
		self._socket.listen(MAX_CLIENTS)
		self.accept(timer)

	# non-blocking accept
	#	cf. http://bit.ly/1orQCxV, http://bit.ly/XXjlWe
	def accept(self, timer):
		if(not self._socket):
			return
		self.timer = timer
		while(self.timer):
			r, w, e = select.select(self.clients, [], [], 1)
			if(not r):
				pass
			else:
				# deal with new client
				for s in r:
					if(s == self._socket):
						c, a = self._socket.accept()
						self.clients.append(c)
					else:
						data = s.recv(100)
						if(data):
							s.send(data)
						else:
							s.close()
							self.clients.remove(s)
			if(self.timer > 0):
				self.timer -= 1

	def stop(self):
		if(not self._socket):
			return
		self.timer = 0
		self._socket.shutdown(0)
		self._socket.close()
