class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}

        for i in range(0, len(s), 1):
            if s[i] in countS:
                countS[s[i]] += 1
            else:
                countS[s[i]] = 1
        
        for j in range(0, len(t), 1):
            if t[j] in countS:
                if countS[t[j]] > 1:
                    countS[t[j]] -= 1
                else:
                    del countS[t[j]]
            else:
                return False
        
        if len(countS) == 0:
            return True
        else:
            return False
        
        
