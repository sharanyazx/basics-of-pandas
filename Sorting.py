print("  SORTING A SERIES  ")
s1= pd.Series([10,50,30,90,40])
print("ORIGINAL SERIES  IS   :",s1)
sort=s1.sort_values()
print("SORTED SERIES IS :",sort)

print(''' SORTING OF INDEX ''')
indexsort= pd.Series([10,20,30,40,50],index=[2,1,5,3,4]) 
print("sorted index :",indexsort.sort_index())

