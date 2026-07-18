class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums: List[int], left: int, right: int):
            if left == right:
                return
            mid = (left + right) // 2
            mergeSort(nums, left, mid)
            mergeSort(nums, mid + 1, right)
            merge(nums, left, mid, right)
        
        def merge(nums: List[int], left: int, mid: int, right: int):
            low = left
            high = mid + 1
            temp = list()
            while low <= mid and high <= right:
                if nums[low] < nums[high]:
                    temp.append(nums[low])
                    low += 1
                else:
                    temp.append(nums[high])
                    high += 1
                
            while low <= mid:
                temp.append(nums[low])
                low += 1
            while high <= right:
                temp.append(nums[high])
                high += 1
            
            for i in range(len(temp)):
                nums[left + i] = temp[i]
            
        mergeSort(nums, 0, len(nums) - 1)
        return nums