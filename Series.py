
print(''' WORKING WITH SERIES IN PANDAS ALONG WITH NUMPY ''')
import numpy as np
index=np.array(['a','b','c','d','e'])
a=np.array([10,20,30,40,50])
b=pd.Series(a,index=index)
print(b)
