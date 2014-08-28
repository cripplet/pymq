import unittest

from pymq.classes.queue import MessageQueue
from pymq.classes.item import MessageItem

class TestQueueBasic(unittest.TestCase):
	def setUp(self):
		self.q = MessageQueue(tag='TEST')

	def test_init(self):
		pass

	def test_push(self):
		self.q.push(MessageItem(eid=1111))
		self.assertEqual(self.q.pop().eid, 1111)
