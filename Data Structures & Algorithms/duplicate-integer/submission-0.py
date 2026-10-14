class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = []
        for i in nums:
            if i not in nums_set:
                nums_set.append(i)
            else:
                return True
        return False
        