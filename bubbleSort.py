arr = [5,9,3,1,2,8,4,7,6]
print('before sorting',arr)
n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1] :
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
print('after sorting',arr)