import unittest

from pymq.classes.server import MessageServer

class TestServerBasic(unittest.TestCase):
	def setUp(self):
		self.s = MessageServer()

	def test_init(self):
		self.s.start(1)
		self.s.stop()
