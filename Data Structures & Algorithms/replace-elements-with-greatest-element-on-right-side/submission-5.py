class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestNum = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = greatestNum
            greatestNum = max(temp, greatestNum)
        return arr