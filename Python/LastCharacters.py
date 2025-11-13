#The last 3 characters in each element of the object "codes" below are 2 digit alpha codes representing a country. Extract these codes into a new list called alpha2 
codes = ['826GBR','840USA','276DEU','818EGY','250FRA']
alpha2 = list(map(lambda x: x[-3:], codes))
print(alpha2)