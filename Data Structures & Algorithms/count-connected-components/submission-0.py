class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[]for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(adj, s, visited):
            q = deque()
            q.append(s)
            visited[s] = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True

        def BSTD (adj):
            visited = [False]*n
            res = 0

            for i in range(n):
                if not visited[i]:
                    res+=1
                    bfs(adj, i, visited)

            return res

        return BSTD(adj)