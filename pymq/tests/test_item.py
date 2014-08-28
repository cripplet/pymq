import unittest

from pymq.classes.item import MessageItem

class TestItemBasic(unittest.TestCase):
	def setUp(self):
		self.i = MessageItem()

	def test_init(self):
		pass
