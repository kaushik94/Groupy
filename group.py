import types

def check_if_group(group, function):
	if not len(group):
		return False, "the set is empty"
	if not _check_associvity(group, function):
		return False, "the function is not associative on the group elements"
	if not _check_closure(group, function):
		return False, "the function is not closed"

class Group():
	def __init__(self, group, function=None):
		self.is_multiplicative = False
		if function is None:
			self.is_multiplicative = True
			pass
		elif not isinstance(function, types.FunctionType):
			raise TypeError('should supply a function')
		self.group = group
		self.function = function

	def cayley_table(self):
		raise NotImplementedError

	@property
	def isFinite(self):
		return True

	@property
	def isAbelian(self):
		raise NotImplementedError

	@property
	def order(self):
		raise NotImplementedError

	@property
	def is_Multiplicative(self):
		return self.is_multiplicative
