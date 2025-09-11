import pandas as pd
import numpy as np

e={'name':['dian','jhon','obito','sam','emily','matthew','micheal','ben','gwen','kevin'],'score':[13,24,23,np.nan,8,25,20,23,np.nan,18],
   'attempt':[1,2,3,4,1,2,3,1,2,1],
   'qualify':['yes','no','yes','yes','no','no','yes','yes','no','yes']}

lbl=['a','b','c','d','e','f','g','h','i','j']
d= pd.DataFrame(e)
print("summary of the info abt this dataframe and its data:")
print(d.info())

