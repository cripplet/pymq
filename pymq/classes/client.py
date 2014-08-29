class MessageClient(object):
	def __init__(self, *args, **kwargs):
		self.server_ip = None
		self.out_port = None
		self.__dict__.update(kwargs)
		super(MessageClient, self).__init__()
