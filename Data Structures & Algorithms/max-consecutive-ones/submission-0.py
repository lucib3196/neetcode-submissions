class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for n in nums:
            if n != 1:
                max_count = count if count > max_count else max_count
                count = 0
                
            else:
                count+=1
            
        
        result = max(max_count,count)
        return result
        