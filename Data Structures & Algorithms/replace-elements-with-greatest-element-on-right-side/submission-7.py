class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestEle = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = greatestEle
            greatestEle = max(greatestEle, temp)
        
        return arr