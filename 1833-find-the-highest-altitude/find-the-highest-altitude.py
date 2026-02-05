class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        max_arr = [0]
        for i in gain:
            highest_altitude += i
            max_arr.append(highest_altitude)
        return max(max_arr)