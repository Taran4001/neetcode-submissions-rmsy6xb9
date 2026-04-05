class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        ans = []
        for i in range(1, len(arr)):
            maxNum = -1
            if i == len(arr) - 1:
                ans.extend([arr[-1], -1])
                return ans
            for j in range(i, len(arr)):
                maxNum = max(arr[j], maxNum)
            ans.append(maxNum)
        return ans