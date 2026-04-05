class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                ans[len(arr) - 1] = -1
            else:
                ans[i] = max(arr[i + 1], ans[i + 1])

        return ans

