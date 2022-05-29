def selection_sort(array,n):
    for i in range (n-1):
        
        min=i
        #loops through the array elements
        for j in range(i+1, n):
            #compares two adjacent array element
            if array[j] < array[min]:
               min=j
            # swaps the two elements
               (array[i], array[min]) = (array[min], array[i])

    return array
array = [1,4,6,3,7,9]
print(selection_sort(array, len(array)))


