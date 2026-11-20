class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not len(nums):
            return 0
        pt, pe = 0, len(nums)-1
        while (pt <= pe):
            # Edge case
            if nums[pe] == val:
                pe-=1
            if nums[pt] == val:
                nums[pt], nums[pe] = nums[pe], nums[pt]
                pe-=1
            else:
                pt+=1
        return pt
        