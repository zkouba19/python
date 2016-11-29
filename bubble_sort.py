def bubblesort(arr):
	for k in range (len(arr)-1):
		for i in range (len(arr)-1):
			if arr[i] > arr[i + 1]:
				temp = arr[i]
				arr[i] = arr[i + 1]
				arr[i + 1] = temp
	return arr

print bubblesort([3, 20, 5, 10, 7, 60, 5])