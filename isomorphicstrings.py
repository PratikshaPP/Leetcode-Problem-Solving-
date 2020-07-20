# Time Complexity : O(N2)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :Came up with a brute force solution using hashing but not very satisfied with it
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        iso_map = {}
        
        
        for i in range(len(t)):
            if iso_map == {}:
                iso_map[s[i]] = t[i]
                continue
            
            if s[i] not in iso_map.keys():
                if t[i] in iso_map.values():
                    return False
                else:
                    iso_map[s[i]] = t[i]
            else:
                if t[i] in iso_map.values():
                    if iso_map[s[i]]!=t[i] :
                        return False
                else:
                    return False
                
        return True
                
                    
        
            
           
        