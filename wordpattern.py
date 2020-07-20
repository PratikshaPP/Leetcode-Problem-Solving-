# Time Complexity : O(N2)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Came up with a brute force solution using hashing but not very satisfied with it


from collections import defaultdict
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        iso_map = {}
        
        str_array = str.split()
        if len(pattern)!=len(str_array):
            return False
        for i in range(len(str_array)):
            if iso_map == {}:
                iso_map[pattern[i]] = str_array[i]
                continue
            
            if pattern[i] not in iso_map.keys():
                if str_array[i] in iso_map.values():
                    return False
                else:
                    iso_map[pattern[i]] = str_array[i]
            else:
                if str_array[i] in iso_map.values():
                    if iso_map[pattern[i]]!=str_array[i] :
                        return False
                else:
                    return False
                
        return True
        
        
        