import unittest

from pymq.classes.item import MessageItem

class TestItemBasic(unittest.TestCase):
	def setUp(self):
		self.i = MessageItem(eid='unique')

	def test_init(self):
		self.assertEqual(self.i, MessageItem(eid='unique'))
		self.assertNotEqual(self.i, MessageItem(eid='not_unique'))
