class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        def dfs(node, parent):
            visited[node] = True

            for nei in adj[node]:
                if not visited[nei]:
                    if dfs(nei, node):
                        return True
                elif nei != parent:
                    return True

            return False

        # Detect cycle
        if dfs(0, -1):
            return False

        # Ensure graph is connected
        return all(visited)