class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_prereq = [[False] * numCourses for _ in range(numCourses)]
        for pre, course in prerequisites:
            is_prereq[pre][course] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_prereq[i][k] and is_prereq[k][j]:
                        is_prereq[i][j] = True
        return [is_prereq[u][v] for u, v in queries]   