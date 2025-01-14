class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        result = 0
        
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                left = right = i
                
                while left > 0 and arr[left] > arr[left-1]:
                    left -= 1
                    
                while right < len(arr)-1 and arr[right] > arr[right+1]:
                    right += 1
                    
                result = max(result,(right-left+1))  
                
        return result        
        