class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        if len(d) == 1:
            return 1
        half = len(arr) // 2
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        cur = 0
        for count, (_, val) in enumerate(d):
            if cur >= half:
                return count
            cur += val