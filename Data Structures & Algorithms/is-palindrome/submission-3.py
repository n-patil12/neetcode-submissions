class Solution:
    def isPalindrome(self, s: str) -> bool:
        word_dict = {}
        word_dict2 = {}

        count = 0
        for i in range(0, len(s), 1):
            if s[i].isalnum():
                curr_letter = s[i].lower()
                word_dict[count] = curr_letter
                count += 1 

        count2 = 0        
        for j in range((len(s) - 1), -1, -1):
            if s[j].isalnum():
                curr_letter2 = s[j].lower()
                word_dict2[count2] = curr_letter2 
                count2 += 1
    
        # print(len(s))
        print(word_dict)
        print(word_dict2)
        # print(repr(s))
    
        if word_dict == word_dict2:
            return True
        else:
            return False
            
