array = [2,4,6,8,1,5,7,3,9]
for i in range(1,len(array)):
    x = array[i]
    idx = i
    while idx >0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x
print(array)