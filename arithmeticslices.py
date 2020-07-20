# Time Complexity : O(N)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        right = 0
        count = 0
        sum = 0
        for i in reversed(range(n-2)):
            
            if A[i+1]-A[i] == A[i+2]-A[i+1]:
                count =right+1
                right = count
                sum +=right    
            else:
                right = 0          
        return sum
                
                
        