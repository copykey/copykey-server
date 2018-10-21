from copykey import find_rectangle

def gen_pts(min, max):
	for x in range(min, max):
		for y in range(min, max):
			yield (x, y)

#try and get normalize_points to throw an assertion error by brute force
for a in gen_pts(0, 10):
	for b in gen_pts(0, 10):
		for c in gen_pts(0, 10):
			for d in gen_pts(0, 10):
				pts = [[a], [b], [c], [d]]
				print(pts)
				find_rectangle.normalize_points(pts)
