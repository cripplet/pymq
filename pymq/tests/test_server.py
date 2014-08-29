import socket
import threading
import unittest

from pymq.classes.server import MessageServer

class TestServerBasic(unittest.TestCase):
	def setUp(self):
		self.s = MessageServer()
		self.t = threading.Thread(None, self.s.start)
		self.t.start()

	def tearDown(self):
		self.s.stop()
		self.t.join()

	def test_listen(self):
		q = MessageServer()
		q.send('ABC', 'localhost')
		q.send('DEF', 'localhost')
