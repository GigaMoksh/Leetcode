class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbours = defaultdict(list)
        for edge in edges:
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])

        q = deque()
        q.append(source)
        visited = set()
        visited.add(source)
        
        while q:
            node = q.pop()
            if node == destination:
                return True
            for no in neighbours[node]:
                if no not in visited:
                    visited.add(no)
                    q.append(no)
        return False
                    