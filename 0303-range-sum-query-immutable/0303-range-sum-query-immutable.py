class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        self.sumLeft = 0
        for i in range(len(nums)):
            self.sumLeft += nums[i]
            self.prefixSum.append(self.sumLeft)


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right]- self.prefixSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)