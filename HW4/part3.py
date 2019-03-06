def mergeK(arr):
    lastList=len(arr)-1 #Assign the lastList to a variable
    while(lastList!=0): #Loop until 1 list left
        i=0
        j=lastList
        while(i<j): #Loop until all pairs merged - Merge arrays till the list length halved
            arr[i] = mergeTwo(arr[i], arr[j], []) 
            i=i+1
            j=j-1
            if(i>=j):
                lastList=j
    return arr[0]  #Return 0th index because only 1 merged array left
            
            
def mergeTwo(arr1, arr2, result):
    if not arr1 or not arr2:    #If one of the array is empty add the rest of the other array to the result
        result = result + arr1 + arr2
    elif arr1[0]<=arr2[0]:
        result.append(arr1[0])
        return mergeTwo(arr1[1:], arr2, result)
    elif arr1[0]>arr2[0]:
        result.append(arr2[0])
        return mergeTwo(arr1, arr2[1:], result)
    return result

print(mergeK([[1,4,3], [1,2,22], [2,8,9], [7, 16, 21]]))