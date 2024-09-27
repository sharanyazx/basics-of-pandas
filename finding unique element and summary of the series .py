print(''' DISPLAYING UNIQUE FUNCTION''')
s1= pd.Series([50,30,10,50,30,90,40,90,99,7])
unique=s1.unique()
print("unique elements :", unique)


'''TO FIND NO.OF UNIQUE ELEMENTS (nunique)'''
noofunique=s1.nunique()
print("no of unique",noofunique)

print("    SUMMARY OF THE SERIES    ")
s1= pd.Series([10,20,30,40,50])
summary=s1.describe()
print("summary of the series  :",summary)
