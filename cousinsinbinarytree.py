# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root == None:
            return False
    
        queue = deque()
        queue.append(root)
        depthX = 0
        depthY = 0
        depth = 0
        parentX = None
        parentY = None
        while queue:
            count = len(queue)
            depth = depth+1
            for i in range(count):
                element = queue.popleft()
                if element.left!=None:
                    queue.append(element.left)
                    if element.left.val == x:
                        parentX = element
                        depthX = depth
                    elif element.left.val == y:
                        parentY = element
                        depthY = depth 
                if element.right!=None:
                    queue.append(element.right)
                    if element.right.val == x:
                        parentX = element
                        depthX = depth
                    elif element.right.val == y:
                        parentY = element
                        depthY = depth 
                                     
        return self.checkValidity(parentX, parentY, depthX, depthY)
            
        
        
    def checkValidity(self, parentX, parentY, depthX, depthY):
        
        return parentX!=parentY and depthX==depthY
        