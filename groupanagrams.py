# Time Complexity : O(NK)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
Improved solution using product of Primes technique


from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        result = []
        anagrams = defaultdict(list)
        
        for word in strs:
            anagrams[self.computePrimeProduct(word,primes)].append(word)
            
        for value in anagrams.values():
            result.append(value)
            
        return result
            
    def computePrimeProduct(self,word,primes):
        product = 1
        for i in range(len(word)):
            product = product*primes[ord(word[i]) - ord('a')]
        return product
        