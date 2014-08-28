import unittest

from pymq.classes.item import MessageItem

class TestItemBasic(unittest.TestCase):
	def setUp(self):
		self.i = MessageItem()

	def test_filename(self):
		self.assertRaises(AttributeError, self.i.filename)
		self.i.eid = 'foo'
		assertTrue(None)
