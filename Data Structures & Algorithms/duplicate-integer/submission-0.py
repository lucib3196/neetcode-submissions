class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = dict()
        for n in nums:
            val = counts.get(n,0)
            if val>0:
                return True
            counts[n] = val+1
        return False