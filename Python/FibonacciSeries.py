#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n==0:
            return 0
        elif n==1:
            return 1
        fib = [0,1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]
object = Solution()
print(object.nthFibonacci(7))

####################################################################
####################################################################
#time complexity: O(2ⁿ)
class Solution1: 
    
    def nthFibonacci1(self, n: int) -> int: 
        if n==0: 
            return 0 
        elif n==1: 
            return 1 
        else: 
            return self.nthFibonacci1(n-1) + self.nthFibonacci1(n-2)
obj=Solution1()
print(obj.nthFibonacci1(7))