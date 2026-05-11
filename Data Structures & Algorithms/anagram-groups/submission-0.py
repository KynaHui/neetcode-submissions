from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map count of char to list of Anagrams
        results = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a to z 

            for char in s:
                count[ord(char) - ord("a")] += 1
                # count: type list
            
            results[tuple(count)].append(s)
        
        return list(results.values())