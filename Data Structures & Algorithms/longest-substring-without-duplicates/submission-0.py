class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0 
        my_set = set()
        longest = 0

        while (right < len(s)):
            my_set.add(s[left])
            my_set.add(s[right])
            right += 1

            if (len(my_set) > longest):
                longest = len(my_set)

            while right < len(s) and s[right] in my_set:
                my_set.remove(s[left])
                left += 1
    
        return longest
            
            