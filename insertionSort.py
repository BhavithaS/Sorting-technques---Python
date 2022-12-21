arr = [5,9,3,1,2,8,4,7,6]
n = len(arr)

for i in range(1,n) :
    temp = arr[i]
    j = i-1
    while j >= 0 and arr[j] > temp :
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = temp
print('after sort' , arr)