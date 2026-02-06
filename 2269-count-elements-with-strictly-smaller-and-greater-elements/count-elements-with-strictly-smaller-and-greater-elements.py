class Solution:
    def countElements(self, nums: List[int]) -> int:
        minE = min(nums)
        maxE = max(nums)
        return sum(1 for num in nums if minE < num < maxE)