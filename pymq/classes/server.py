import select
import socket
import sys

from pymq.settings import HOST as HOST
from pymq.settings import MAX_CLIENTS as MAX_CLIENTS
from pymq.settings import PORT as PORT
from pymq.settings import VERSION as V

class MessageServer(object):
	def __init__(self, *args, **kwargs):
		self.host = None
		self.port = PORT
		self.__dict__.update(kwargs)
		self.incoming = []
		self._server = None	# listen for incoming connections
		self._client = None	# output data stream
		super(MessageServer, self).__init__()

	def start(self):
		self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self._server.bind((HOST, self.port))
		self._server.listen(MAX_CLIENTS)
		self.accept()

	# non-blocking accept
	#	cf. http://bit.ly/1orQCxV, http://bit.ly/XXjlWe
	def accept(self):
		self._accept_flag = True
		while(self._accept_flag):
			r, w, e = select.select([ self._server ], [], [], 1)
			if(r):
				c, a = self._server.accept()
				print(a)
				buf = ''
				msg = ''
				length = None
				while(length == None):
					print('while len == None')
					buf += str(c.recv(1024))
					if(buf == ''):
						break
					if(':' in str(buf)):
						l, throwaway, buf = buf.partition(':')
						length = int(l)
						msg = buf[:length]
						length -= len(buf)
						if(length < 0):
							raise(KeyError)
						break
				while(length > 0):
					buf = c.recv(1024)
					if(buf == ''):
						break
					msg += buf[:length]
					length -= len(buf)
				print(msg)
				c.shutdown(0)
				c.close()
		self._stop_flag = False

	def send(self, msg, host=None):
		if(not host):
			host = self.host
		self.host = host

		self._client = socket.create_connection((host, PORT), 1)
		if(not self._client):
			raise(KeyError)
		self._client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self._client.send('%s:' % str(len(msg)))
		if(V == 2):
			self._client.send(msg)
		else:
			self._client.send(bytes(msg, 'UTF-8'))
		self._client.shutdown(0)
		self._client.close()

	def stop(self):
		if(not self._server):
			return
		self._stop_flag = True
		self._accept_flag = False
		# wait for the final loop
		while(self._stop_flag):
			pass
		self._server.shutdown(0)
		self._server.close()
