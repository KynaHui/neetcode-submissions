class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # data structure in Python, build hash map
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            # countS.get(key, default_value), key not exist, return default
            # countS[s[i]] += 1 -> wrong, no initalize 
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        # if countS != countT: # faster a bit
        #     return False
        for c in countS: # better for interview, manual check 
            if countS[c] != countT.get(c, 0):
                return False
        return True