def dot_product(vector_x, vector_v):
	x = vector_x
	v = vector_v

	vector_product = []
	if len(x) == len(v):
		for x_index, x_number in enumerate(x):
			for v_index, v_number in enumerate(v):
				if x_index == v_index:
					product = x_number*v_number
					vector_product.append(product)

		return sum(vector_product)
	else:
		return False


def find_projection(vector_x, vector_v):
	x = vector_x
	v = vector_v
	w = []
	# when w = x-k(v)
	# and w.v = 0
	# using (x - kv).v = 0


	# step 1) find k given x vector and v vector using k = (x.v)/(v.v)
	# step 2) find w after finding k with w = x - k(v)

	k_nominator = dot_product(x, v)
	k_denominator = dot_product(v, v)

	k = k_nominator/k_denominator

	k_v = []

	for v_number in v:
		k_v.append(v_number*k)

	for x_index, x_number in enumerate(x):
		for k_v_idx, k_v_num in enumerate(k_v):
			if x_index == k_v_idx:
				w.append(x_number - k_v_num)

	return w

print find_projection([10, 2, 1], [1, 1, -1]) 