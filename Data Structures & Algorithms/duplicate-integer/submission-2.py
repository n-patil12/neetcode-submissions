class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr_set = set()

        for i in range(0, len(nums), 1):
            if nums[i] in curr_set:
                return True
            else:
                curr_set.add(nums[i])
        
        return False