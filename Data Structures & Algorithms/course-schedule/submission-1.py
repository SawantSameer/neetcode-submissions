class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[]for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            adjList[prerequisites[i][1]].append(prerequisites[i][0])

        # Function to detect a cycle in a directed graph

        def isCyclicUtil(v, visited, recStack):

            # Mark current node as visited and 
            # adds to recursion stack
            visited[v] = True
            recStack[v] = True

            # Recur for all neighbours
            # if any neighbour is visited and in 
            # recStack then graph is cyclic
            for neighbour in adjList[v]:
                if visited[neighbour] == False:
                    if isCyclicUtil(neighbour, visited, recStack) == True:
                        return True
                elif recStack[neighbour] == True:
                    return True

            # The node needs to be popped from 
            # recursion stack before function ends
            recStack[v] = False
            return False


        def isCyclic():
            visited = [False]*numCourses
            recStack = [False]*numCourses
            for i in range(numCourses):
                if not visited[i]:
                    if isCyclicUtil(i, visited, recStack):
                        return True

            return False

        return not isCyclic()