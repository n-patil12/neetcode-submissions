# Resource 1. searched up how to add values into a set
# Reosurce 2. search up if a set can be used as a key in a map
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returned_sublist = []
        if len(strs) == 1:
            returned_sublist.append(strs)
        else:
            strs_map = {}
            for curr_str in strs:
                curr_str_map = {}
                for curr_letter in curr_str:
                    if curr_letter in curr_str_map:
                        curr_str_map[curr_letter] += 1
                    else:
                        curr_str_map[curr_letter] = 1

                curr_str_set = frozenset(curr_str_map.items())
                if curr_str_set in strs_map:
                    strs_map[curr_str_set].append(curr_str)
                else:
                    strs_map[curr_str_set] = []
                    strs_map[curr_str_set].append(curr_str)
            
            for key, value in strs_map.items():
                returned_sublist.append(value)

        return returned_sublist
