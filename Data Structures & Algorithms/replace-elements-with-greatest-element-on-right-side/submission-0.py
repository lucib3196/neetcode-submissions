class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i, n in enumerate(arr):
            sub = arr[i+1:]
            if len(sub):
                arr[i] = max(sub)
            else:
                arr[i] = -1
        return arr

            
        