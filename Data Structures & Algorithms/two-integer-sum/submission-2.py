class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            find_num = target - nums[i]
            if find_num in nums and i != nums.index(find_num):
                list = [i, nums.index(find_num)]
                list.sort()

                return list
