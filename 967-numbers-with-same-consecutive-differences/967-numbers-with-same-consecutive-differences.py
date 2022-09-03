class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        if n == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        res = []
        def backtrack(n, num):
            if n == 0:
                return res.append(num)
            
            d = num % 10
            next_ = set([d - k, d + k])
            
            for x in next_:
                if 0 <= x < 10:
                    numm = num * 10 + x
                    backtrack(n - 1, numm)

        for x in range(1, 10):
            backtrack(n - 1, x)
            
        return res