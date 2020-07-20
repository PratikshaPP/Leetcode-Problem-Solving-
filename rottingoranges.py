# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

from collections import deque
class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        time = -1
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
              
        while queue:
            count = len(queue)
            time +=1
            for i in range(count):
                element = queue.popleft()
                x = element[0]
                y = element[1]
                for k in range(4):
                    if self.isValid(x+dx[k], y+dy[k], m, n) and grid[x+dx[k]][y+dy[k]]==1:
                        grid[x+dx[k]][y+dy[k]] = 2
                        queue.append((x+dx[k], y+dy[k]))
                        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
        if time == -1:
            return 0
        else:
            return time
                    
                    
    def isValid(self, x, y, m, n):
        return x>=0 and x<m and y>=0 and y<n