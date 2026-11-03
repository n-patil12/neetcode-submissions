class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[i] = nums[i]

        for curr_index in range(len(nums)):
            if (target - nums[curr_index]) in nums:
                complement = target - nums[curr_index]
                for k, v in my_dict.items():
                    if complement == v and k != curr_index:
                        found_index = k
                        return sorted([found_index, curr_index])
                