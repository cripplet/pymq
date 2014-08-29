from pymq.settings import VERSION as V
if(V == 2):
	import Queue as queue
else:
	import queue

import time

from pymq.classes.item import MessageItem

class MessageQueue(object):
	def __init__(self, *args, **kwargs):
		self.eid = None
		self.tag = None

		self.delta = 60
		self.clock = time.time()

		self.__dict__.update(kwargs)

		self.q = queue.Queue()
		self.p = {}

		super(MessageQueue, self).__init__()

	def push(self, val):
		self.q.put(val)
		self.cleanup()

	def pop(self):
		if(self.q.empty()):
			return(None)
		else:
			val = self.q.get()
			val.init_time = time.time()
			val.drop_time = val.init_time + self.delta
			self.p[val.eid] = val
			return(val)
		self.cleanup()

	def confirm(self, eid):
		try:
			self.p.pop(eid)
		except KeyError:
			pass
		self.cleanup()

	def invalidate(self, eid):
		try:
			self.push(self.p.pop(eid))
		except KeyError:
			raise(KeyError)

	def cleanup(self):
		if(self.clock + self.delta > time.time()):
			return
		for k, v in self.p.items():
			if(v.drop_time > (self.clock + self.delta)):
				self.invalidate(k)
		self.clock = time.time()
