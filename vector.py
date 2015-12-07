class Vector():
	def __init__(dim = 2, val = []):
		self.vals = []
		self.dim = dim
		if val and len(val) == dim:
			for i in range(dim):
				self.vals.append(val[i])

		elif not val:
			for i in range(dim):
				self.vals.append(0)

		else:
			print "Error 1: wrong dim"
			exit()

	def __init__(vector):
		self.dim = vector.dim
		self.vals = list(vector.vals)

	def value_mult(a):
		for i in self.vals:
			i *= a

	def value_div(a):
		for i in self.vals:
			i /= a

	def value_add(a):
		for i in self.vals:
			i += a

	def value_sub(a):
		for i in self.vals:
			i -= a

	def value_pow(a):
		for i in self.vals:
			i **= a

	def add(v):
		if v.dim != self.dim:
			print "Error 2: wrong dim"
			exit()

		for i in range(self.dim):
			self.vals[i] += v.vals[i]

	def sub(v):
		if v.dim != self.dim:
			print "Error 2: wrong dim"
			exit()

		for i in range(self.dim):
			self.vals[i] -= v.vals[i]


	def scalar_div(v):
		if v.dim != self.dim:
			print "Error 2: wrong dim"
			exit()

		for i in range(self.dim):
			self.vals[i] /= v.vals[i]


	def scalar_mult(v):
		if v.dim != self.dim:
			print "Error 2: wrong dim"
			exit()

		for i in range(self.dim):
			self.vals[i] /= v.vals[i]


	def sqdist(v):
		if v.dim != self.dim:
			print "Error 2: wrong dim"
			exit()

		ret = 0
		for i in range(self.dim):
			ret += (self.vals[i] - v.vals[i]) ** 2
		return ret

