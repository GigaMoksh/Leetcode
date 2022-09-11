class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = list(zip(efficiency, speed))
        engineers.sort(reverse=True)  # Sort by decreasing order of efficiency
        minHeap = []
        speedSum = 0
        ans = 0
        for e, s in engineers:
            speedSum += s
            heappush(minHeap, s)
            if len(minHeap) > k:  # Over k engineers -> remove the lowest speed engineer
                speedSum -= heappop(minHeap)
            ans = max(ans, speedSum * e)
        return ans % 1_000_000_007