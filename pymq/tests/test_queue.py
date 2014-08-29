import unittest
import time

from pymq.classes.queue import MessageQueue
from pymq.classes.item import MessageItem

class TestQueueBasic(unittest.TestCase):
	def setUp(self):
		self.q = MessageQueue(tag='TEST')

	def test_init(self):
		pass

	def test_push(self):
		self.assertEqual(self.q.pop(), None)
		self.q.push(MessageItem(eid=1111))
		self.assertEqual(self.q.pop(), MessageItem(eid=1111))
		try:
			self.q.invalidate(1111)
		except KeyError:
			self.fail()
		self.assertEqual(self.q.pop(), MessageItem(eid=1111))
		try:
			self.q.confirm(1111)
		except KeyError:
			self.fail()
		self.assertEqual(self.q.pop(), None)
		self.q.delta = 1
		self.q.push(MessageItem(eid=1111))
		self.assertEqual(self.q.pop(), MessageItem(eid=1111))
		time.sleep(2)
		self.assertEqual(self.q.pop(), MessageItem(eid=1111))
