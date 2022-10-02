from collections import deque

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = [[]*n for _ in range(n)]
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [0 for _ in range(n)]
        # print(visited)
        # print(graph)
        q = deque([])
        q.append(0)
        
        visited[0] = 1
        cnt = 1
        
        for rt in restricted:
            visited[rt] = -1
        
        while q:
            node = q.popleft()
            for new in graph[node]:
                # if visited[new] == 0 and new not in restricted:
                if visited[new] == 0:
                    q.append(new)
                    visited[new] = 1
                    cnt += 1
                # print(node, new)
                
        return cnt
            
        