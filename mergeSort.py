
def mergeSort(arr):
    if len(arr)> 1 :
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        #calling recursively for breaking
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i<len(left) and j<len(right) :
            if left[i] < right[j] :
                arr[k] = left[i]
                i += 1
                k += 1
            else :
                arr[k] = right[j]
                j += 1
                k += 1
        
        while i < len(left) :
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right) :
            arr[k] = right[j]
            j +=1
            k += 1

arr = [5,9,3,1,2,8,4,7,6]
n = len(arr)
mergeSort(arr)
print(arr)