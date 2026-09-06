class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = [[]for _ in range(numCourses)]

        for src, dst in prerequisites:
            indegree[src]+=1
            adj[dst].append(src)

        q = deque()
        for n in range(numCourses):
            if indegree[n]==0:
                q.append(n)

        finish = 0
        res = []

        while q:
            node = q.popleft()
            finish += 1
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if not indegree[nei]:
                    q.append(nei)


        if finish == numCourses:
            return res
        return []