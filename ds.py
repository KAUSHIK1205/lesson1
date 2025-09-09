import numpy as np
datatype=[('name','S15'),('class',int),('height',float)]
sd=[('jame',5,48.5),('nail',7,23.3),('ben',3,32.14)]
s=np.array(sd,dtype=datatype)
print("orginal array:",s)
print ("sort by height")
print(np.sort(s,order='height'))