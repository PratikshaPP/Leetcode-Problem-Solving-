# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0
        
        
        employeesdict = {}
        for employee in employees:
            employeesdict[employee.id] = employee
            
        queue = deque()
        queue.append(id)
        
        while queue:
            count = len(queue)
            for i in range(count):
                k = queue.popleft()
                total +=employeesdict[k].importance
                subordinates = employeesdict[k].subordinates
                for sub in subordinates:
                    queue.append(sub)
        return total
            
                
            
        
            
        