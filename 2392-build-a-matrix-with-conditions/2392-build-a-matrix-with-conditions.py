class Solution:
    def buildMatrix(self, k: int, R: List[List[int]], C: List[List[int]]) -> List[List[int]]:
        def getOrder(A):
            nxt, indegree = [set() for _ in range(k)], [0] * k
            seen, dq, ans = set(), collections.deque(), []
            A = set([tuple(a) for a in A])  
            for i, j in A:
                nxt[i - 1].add(j - 1)
                indegree[j - 1] += 1
            for i in range(k):
                if indegree[i] == 0:
                    dq.append(i)
                    seen.add(i)    
            while dq:
                cur = dq.popleft()
                ans.append(cur)
                for cand in nxt[cur]:
                    indegree[cand] -= 1
                    if indegree[cand] == 0 and cand not in seen:
                        seen.add(cand)
                        dq.append(cand)       
            return ans if len(seen) == k else []
        
        ans1, ans2 = getOrder(R), getOrder(C)
        if not ans1 or not ans2: return []

        A = [[0] * k for _ in range(k)]
        for i in range(k): A[ans1.index(i)][ans2.index(i)] = i + 1
        return A