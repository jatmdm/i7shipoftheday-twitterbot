import random

i7cast = ["Riku", "Iori", "Yamato", "Mitsuki", "Tamaki", "Nagi", "Sougo", "Yuki", "Momo", "Gaku", "Tenn", "Ryuu"]

def GenerateRandomShip(size=None):
	if size == None:
		size = random.randint(2, 3)

	cast_size = len(i7cast)

	ship = []

	for x in range(size):
		index = random.randint(0, cast_size-1)
		ship.append(i7cast[index])

	return ship