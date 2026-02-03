class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res= []
        for i in range(n):
            if nums[i] > 0:
                break
            if nums[i] == nums[i-1] and i > 0:
                continue
            j = i+1
            k = n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total <0 :
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res           


        