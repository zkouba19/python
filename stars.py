def stars(arr):
	for i in range(0, len(arr)):
		star = "*" * arr[i]
		print star

newarray = [5, 4, 3, 2, 1, 2, 3, 4, 5]
stars_show = stars(newarray)


def stars2(arr):
	for i in range(0,len(arr)):
		if(isinstance(arr[i], int) == True):
			star = "*" * arr[i]
			print star
		else:
			temp = arr[i][0]
			letter = temp * len(arr[i])
			print letter

newarray = [5, "tom", 3, "dojo", 1]
stars_show = stars2(newarray)
