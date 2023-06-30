import numpy as np
l=[1,4,3,7,5,9,56,43]
arr=np.array(l)
print(arr)
print(arr[4])
print(arr[1:5])
arr[0:5]=100
print(arr)
l=[1,4,3,7,5,9,56,43]
arr=np.array(l)

ar=arr[1:4]
print(ar)

ar[:]=99

print(ar)
print(type(arr))


l=[[1,2,3],[3,4,5],[5,6,7]]
arr=np.array(l)
print(arr)

print(arr[0][2])

print(arr[0,2])


print(arr[:2,1:])
print("####")
print(arr[:2])

print(arr>=5)

l=[1,2,3,4,5,6,7,8,9]
arr=np.array(l)
print(arr>5)
b=arr>5
print(arr[b])
#or
print(arr[arr>5])

ar=np.arange(25).reshape(5,5)
print(ar)

print(ar[1:3,3:5])