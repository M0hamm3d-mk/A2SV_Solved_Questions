"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total_iv = 0

        def findEmployee(id):
            for e in employees:
                if e.id == id:
                    return e

        def dfs(e):
            nonlocal total_iv
            total_iv += e.importance
            for s in e.subordinates:
                dfs(findEmployee(s))

        for e in employees:
            if e.id == id:
                dfs(e)
                return total_iv
