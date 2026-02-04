class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        arr.sort()
        n=len(arr)
        k=0
        for i in range(1,n):
            if arr[i]!=arr[k]:
                k+=1
                arr[k]=arr[i]
        return k+1
        