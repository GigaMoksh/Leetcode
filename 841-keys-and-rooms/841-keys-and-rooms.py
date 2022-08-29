class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        
        q = deque()
        q.append(0)
        
        while q:
            node = q.popleft()
            
            for n in rooms[node]:
                if n not in visited:
                    visited.add(n)
                    q.append(n)
        
        return len(visited) == len(rooms)
            