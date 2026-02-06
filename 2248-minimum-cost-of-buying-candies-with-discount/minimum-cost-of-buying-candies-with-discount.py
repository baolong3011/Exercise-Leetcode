class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = []
        n = sorted(cost)
        take = 0
        total = 0
        for i in range(len(n) - 1, -1, -1):
            if take == 2:
                take = 0
            else:
                total += n[i]
                take += 1
        return total