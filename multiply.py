def multiply(a, x):
	for i in range(0, len(a)):
		a[i] = a[i] * x
	return a

newarr = multiply([5, 20, 15, 2], 5)

print newarr