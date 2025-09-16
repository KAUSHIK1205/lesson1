import numpy as np

a=np.arange(9,dtype=np.float64).reshape(3,3)
print('first array')
print(a)
b=np.array([10,10,10])
print('second array')
print(b)

print('add the arrays')
print (np.add(a,b))

print('subtract the arrays')
print(np.subtract(a,b))
print('multiply the arrays')
print(np.multiply(a,b))
print('divide the arrays')
print(np.divide(a,b))