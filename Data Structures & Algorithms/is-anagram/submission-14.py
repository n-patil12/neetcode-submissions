class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        # countT = {}

        for i in range(0, len(s), 1):
            if s[i] in countS:
                countS[s[i]] += 1
            else:
                countS[s[i]] = 0
        
        print(countS)
        
        for j in range(0, len(t), 1):
            if t[j] in countS:
                if countS[t[j]] > 0:
                    countS[t[j]] -= 1
                else:
                    del countS[t[j]]
            else:
                return False
        
        if len(countS) == 0:
            return True
        else:
            return False
        
        # print(len(s))
        # print(len(t))
        # print(len(countS))

        # if len(countS) != 0:
        #     return False
        # else:
        #     return True

        
