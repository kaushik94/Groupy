from group import Group

"""
from group import Set
from group import Function
"""

class FiniteGroup(Group):
	def __init__(self, group, function):
		self.set = group
		self.function = function
		_check_if_group(group, function)
		self.identity = self._find_identity()

	def cayley_table(self):
		cayley = [self.function(a, b) for a in self.set for b in self.set]
		return cayley

	def print_cayley_table(self):
		"""
		Need a better way to print this shit !!
		"""
		print self.cayley_table()

	@property
	def isFinite(self):
		return True

	@property
	def identity(self):
		return self.identity

	@property
	def isAbelian(self):
		if all(self.function(a, b) == self.function(b, a) for a in self.set for b in self.set):
			return True
		return False

	def _find_identity(self):
		for element in self.set:
			if all(element*x == x for x in self.set):
				return element
		raise TypeError('The given set has no identity element on the function')

	@property
	def order(self):
		return len(self.set)


def _check_if_group(group, function):
	if not _check_closure(group, function):
		raise TypeError('The set is not closed under the given function')
	if not  _check_associativity(group, function):
		raise TypeError('The function is not associative on the group')

def _check_closure(group, function):
	if not all(function(a, b)%len(group) in group for a in group for b in group):
		return False
	return True

def _check_associativity(group, function):
	if not all(function(a, function(b, c)) == function(function(a, b), c) for a in group for b in group for c in group):
		return False
	return True
