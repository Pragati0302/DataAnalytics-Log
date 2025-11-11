#Check the status
''' 
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:
    - Either a or b (not both) is non-negative and the flag is false.
    - Both a and b are negative and the flag is true.
Otherwise, return False.
'''

class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if ((a>0) ^ (b>0)) and flag==False:  #^ is the bitwise XOR operator, which returns True only when one of the conditions is True—perfect for “either but not both”.
            return True
        elif (a<0 and b<0) and flag==True:
            return True
        else:
            return False

if __name__ == "__main__":
    obj = Solution()
    result = obj.checkStatus(5, 6, 1)
    print(result)
        

