# here we implement the bubble sort function. Example: How is a list sorted under the hood.

def bubble_sort(array):
        # loop through the range
        for i in range(len(array)):
            # loop until the range minus the last index
            for j in range(0,len(array) - i - 1):
                # checks index 1 greater than index 2 
                if array[j] > array[j+1]:
                    # copies the value to a new variable
                    temp = array[j]
                    # index 2 is placed in index 1
                    array[j] = array[j+1]
                    # index 1 is index 2
                    array[j+1] = temp



numbers = [99, 44, 6,2,1,5,63,87, 283,4,0]
bubble_sort(numbers)
print(numbers)



#Tip: Before writing code, you need to understand how the execution will be.
# If you don't get it at first, learn the concept of bubble sort then return to this function