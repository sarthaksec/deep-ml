import numpy as np

def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	v_arr = np.array(v, dtype=float)
	L_arr = np.array(L, dtype=float)

	scalar = np.dot(v_arr, L_arr) / np.dot(L_arr, L_arr)
	proj = scalar * L_arr
	return [round(x, 3) for x in proj.tolist()]