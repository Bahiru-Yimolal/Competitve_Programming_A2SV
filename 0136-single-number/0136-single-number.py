class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for c,v in count.items():
            if v == 1:
                return c
        