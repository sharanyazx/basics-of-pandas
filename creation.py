print(''' CREATION OF ARRAY USING PANDAS ''')

import pandas as pd
s1= pd.Series([10,20,30,40,50])
print(s1)

print(''' CUSTOMISED INDEX & DEFAULT INDEX ACCESSING ''')
cindex= pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
'''customised index'''
print(cindex['a'])  
'''default index''' 
print(cindex[3])
