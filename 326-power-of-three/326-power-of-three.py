class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def check(n):
            
            if n == 1:
                return True
            
            if n < 1 or n % 3 != 0:
                return False
            
            return check(n // 3)
        
        return check(n)