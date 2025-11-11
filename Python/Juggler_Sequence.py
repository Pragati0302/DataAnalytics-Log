#Juggler's problem
'''
The juggler sequence is a mathematical sequence defined for a starting positive integer a(0). 

Each next term a(n+1) is calculated as follows:
 -> If the current term a(n) is even, a(n+1) would be the floor of the square root of a(n)
-----> i.e., floor of a(n) raised to the power of 1/2

 -> If the current term a(n) is odd, a(n+1) would be the floor of the current term raised to the power 3/2

The sequence continues until it reaches 1.
'''
#Given a number n, find the Juggler Sequence for this number as the first term of the sequence until it becomes 1.
from math import sqrt


class Solution:

    def jugglerSequence(self, n):
        # Initializing the result list with the initial number
        res = [n]

        # Loop until the number becomes 1
        while n > 1:
            # If the number is odd, perform the juggler equation
            if n % 2:
                n = int(sqrt(n) * n)
            # If the number is even, perform the juggler equation
            else:
                n = int(sqrt(n))

            # Add the number to the result list
            res.append(n)

        # Return the final result list
        return res
    
if __name__ == "__main__":
    obj = Solution()
    result = obj.jugglerSequence(9)
    print(result)


