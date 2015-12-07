class Body():
	def __init__(mass, data, speed, location):
		self.mass = mass
		self.data = data
		self.speed = speed
		self.location = location

	def __init__(body):
		self.mass = body.mass
		self.data = body.data
		self.speed = body.speed
		self.location = body.location


	def move(force_vector, time):
		# Update location

		# 1/2at2
		acc_vector = vector.Vector(force_vector)
		acc_vector.value_div(self.mass)
		acc_vector.value_mult(time*time)
		acc_vector.value_div(2)

		# vt
		speed_vector = vector.Vector(self.speed)
		speed_vector.value_mult(time)

		# s = s0 + vt + 1/2at2
		self.location.add(speed_vector)
		self.location.add(acc_vector)

		# Update speed
		acc_vector = vector.Vector(force_vector)
		acc_vector.value_div(self.mass)
		acc_vector.value_mult(time)
		self.speed.add(acc_vector)

	def calc_gravity(body):
		dist = self.location.sqdist(body.location)
		return (6.673E-11 * self.mass * body.mass) / dist