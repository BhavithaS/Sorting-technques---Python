arr = [5,9,3,1,2,8,4,7,6]
n = len(arr)
for i in range(n) :
    currentElement = arr[i]
    min_ = min(arr[i:])
    indexOfEle = arr.index(min_)
    arr[i] , arr[indexOfEle] = min_ , currentElement 

print('after sorting',arr)