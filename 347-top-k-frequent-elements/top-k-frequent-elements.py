class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = []
        for _ in range(len(nums) + 1):
            bucket.append([])
        
        for num, freq in count.items():
            bucket[freq].append(num)

        ans = []
        for freq in range(len(bucket) - 1, -1, -1):
            for num in bucket[freq]:
                ans.append(num)
                if len(ans) == k:
                    return ans