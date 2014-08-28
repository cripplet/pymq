from pymq.settings import TMP_DIR

class MessageItem(object):
	def __init__(self, *args, **kwargs):
		self.eid = None

		self.dat = None
		self.obj = None

		self.init_time = None
		self.drop_time = None

		self._filename = None

		super(MessageItem).__init__(*args, **kwargs)

	@property
	def filename(self):
		if(self._filename == None):
			self._filename = '%s/%s' % (TMP_DIR, self.eid)
		return(self._filename)
