class System():
	def __init__(bodies, tick_timer):
		self.bodies = bodies
		self.tick_timer = tick_timer

	def next_tick():
		new_bodies = []
		for i in self.bodies:
			new_body = body.Body(i)

			# Calculate force vector
			force_vector = vector.Vector()
			for j in self.bodies:
				# Don't want to add itself
				if j != i:
					motion_vector.add(j.calc_gravity(new_body))

			new_body.move(force_vector, self.tick_timer)