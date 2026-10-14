#had to search how to retrieve the max from a dictionary
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        returned_list = []
        elem_map = {}

        for i in nums:
          if i in elem_map:
            elem_map[i] += 1
          else:
            elem_map[i] = 1

        while len(returned_list) < k:
            returned_key = max(elem_map, key=elem_map.get)
            returned_list.append(returned_key)
            elem_map.pop(returned_key)

        return returned_list

