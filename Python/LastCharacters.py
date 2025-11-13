#The last 3 characters in each element of the object "codes" below are 2 digit alpha codes representing a country. Extract these codes into a new list called alpha2 
codes = ['826GBR','840USA','276DEU','818EGY','250FRA']
alpha2 = list(map(lambda x: x[-3:], codes))
print(alpha2)

##LEARNING HERE

'''
At first, I ran the below code!!!
codes = ['826GBR','840USA','276DEU','818EGY','250FRA']
alpha2 = []
alpha2.append(map(x[-3:], codes))
print(alpha2)

Mistakes here: 
1. Map function takes one function as one of its arguments. But I chose to ignore that and just passed x[-3:] which isn't a function. 
2. Map function returns a map object. When I used alpha2.append(map(...)), I passed the whole map object inside it, making alpha2 a map object. 

Hence, it won't work. Printing alpha2 will show such output: <map object at 0x...>


'''