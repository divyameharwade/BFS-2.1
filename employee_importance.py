"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
# ask if one subordinate will have one manager or more
# if 1 manager - n-ary tree - O(n)
# if more managers - graph - O(V+E)
# Space complexity - O(V) -> as we are maintaining refs
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hmap = {}
        for each in employees:
            hmap[each.id] = each
        queue = deque([id])
        importance = 0
        while queue:
            idx = queue.popleft()
            each = hmap.get(idx)
            importance += each.importance
            for sub in each.subordinates:
                queue.append(sub)
        return importance


