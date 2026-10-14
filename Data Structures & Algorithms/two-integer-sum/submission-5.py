class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_set = set()
        for i in range(0,len(nums), 1):
            for j in range(0, len(nums), 1):
                if (nums[i] + nums[j] == target) and (i != j):
                    indices_set.add(i)
                    indices_set.add(j)
                    return list(indices_set)
