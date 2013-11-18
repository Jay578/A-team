#sort the list
# start in the middle of the list
# -if the number is less then that of the middle number in the list
# 	- then start from the begining to the middle and then look at  that middle number
# 	- continue
# -if the number is greater than that of the middle number in the list
# 	- then start from the middle to the end
# 	- look at the middle number
# 	-continue
# return the index of the element if found and -1 otherwise



def bsearch( alist , element):
	alist.sort()
	front = 0
	back = len(alist)-1
	found = True
	midpoint = (front + back)//2

	for i in range(len(alist)):

		if alist[midpoint] == element:
			return midpoint

		elif element > alist[midpoint]:
			front = midpoint + 1
			midpoint = (front + back)//2

		elif element < alist[midpoint]:
			back = midpoint - 1
			midpoint = (front + back)//2

	return -1
