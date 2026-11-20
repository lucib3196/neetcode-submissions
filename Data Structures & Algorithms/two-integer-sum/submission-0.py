class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()
        for i,n in enumerate(nums):
            difference = target-n
            if values.get(difference) is not None:
                return [values.get(difference), i]
            values[n] = i
        return [0,0]