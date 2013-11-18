List = [1, 2, 3, 5, 7, 8, 9, 12, 14, 15, 59, 61, 78, 84]
'''binary search only works on a sorted list. for the sake of this code.
I created a sorted List, hence no need to sort it again.'''
Element = 84
def bsearch(List, Element):
        if List == []:
                print 'empty list'
        else:
                x = len(List)
                q = 0
                first = 0
                last = x-1
                midpoint = (first + last)//2
                for q in range(x):
                        if Element == List[midpoint]:
                                return midpoint
                        elif Element < List[midpoint]:
                                last = midpoint-1
                                midpoint = (first+last)//2
                        elif Element > List[midpoint]:
                                first = midpoint + 1
                                midpoint = (first+last)//2
                        else:
                                return -1
print bsearch(List, Element)
# this Function creates 2 variables 'first' and 'last' as the indices for the first and last value in the list.
# it calculates the midpoint and iterates through a loop that checks if the search element is the same as midpoint
# gives the index for it. if it is not it creates a 'virtual' list (meaning with a different end value or beginning
# value) and then check the mid point again. this keeps going on until the search element is found.
