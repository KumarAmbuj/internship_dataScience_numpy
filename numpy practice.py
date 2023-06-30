import numpy as np
l=[1,2,4,3,6,9]
arr=np.array(l)
print(arr)


import numpy as np
mylist=[1,2,3,4,5,6,7,8]
arr=np.array(mylist)
print(arr)


mylist=[[1,3,5],[4,6,7]]
arr=np.array(mylist)
print(arr)

arr=np.arange(100)
print(arr)

arr=np.arange(0,34,2)
print(arr)

arr=np.zeros(3)
print(arr)

arr=np.zeros((5,5))
print(arr)
arr=np.zeros((2,5))
print(arr)

arr=np.ones((2,5))
print(arr)

arr=np.linspace(0,5,10)
print(arr)


arr=np.eye(3)
print(arr)

arr=np.random.rand(9)
print(arr)

print("##########")
arr=np.random.rand(5,5)
print(arr)
print("##########")

arr=np.random.randn(2)
print(arr)

arr=np.random.rand(4,4)
print(arr)

arr=np.random.randint(1,100,12)
print(arr)

arr=np.array([[1,2,3],[2,3,4]])
ar=arr.reshape(3,2)
print(arr)
print(ar)

l=[1,2,3,4,5,6,7,5,9,8,0,856]
arr=np.array(l)
print(arr)
print("####")
print(arr.max)
print("####")
print(arr.max())

print(arr.min())

print(arr.argmax())

print(arr.argmin())
print(arr.shape)
ar=arr.reshape(3,4)
print(ar)
print(ar.shape)

print(arr.dtype)

from numpy.random import randint
print(randint(3,7))