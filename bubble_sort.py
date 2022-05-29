def bubble_sort(array,n):
    #loops through the array
    for j in range(n-1):
        #loops through the array
        for i in range(n-j-1):
            #compares two adjacent array elements
           if array[i]>array[i+1]:
           #swpaps the two elements
               (array[i],array[i+1])=(array[i+1],array[i])
    return array
array=[1,4,6,3,7,]
print(bubble_sort(array,len(array)))
