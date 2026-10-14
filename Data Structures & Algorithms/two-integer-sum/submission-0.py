class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_sum = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (nums[i] + nums[j] == target):
                    indices_sum.append(i)
                    indices_sum.append(j)
                    return indices_sum  
