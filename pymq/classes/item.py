from pymq.settings import TMP_DIR

class MessageItem(object):
	def __init__(self, *args, **kwargs):
		self.eid = None

		self.dat = None

		self.init_time = None
		self.drop_time = None

		self.__dict__.update(kwargs)
		super(MessageItem, self).__init__()

	def __eq__(self, other):
		return(self.eid == other.eid)

	# tell the server that we are successful
	def callback(self, *args, **kwargs):
		pass
