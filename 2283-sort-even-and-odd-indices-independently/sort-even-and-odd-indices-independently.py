class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd = []
        even = []
        for i in range(n):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        i, j = 0, 0
        for k in range(n):
            if k % 2 == 0:
                nums[k] = even[i]
                i += 1
            else:
                nums[k] = odd[j]
                j += 1
        return nums 