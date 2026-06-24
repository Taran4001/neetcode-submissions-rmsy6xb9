class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums, low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            mergeSort(nums, low, mid)
            mergeSort(nums, mid + 1, high)
            merge(nums, low, mid, high)
        
        def merge(nums, low, mid, high):
            temp = list()
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if nums[left] < nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left <= mid:
                temp.append(nums[left])
                left += 1
            
            while right <= high:
                temp.append(nums[right])
                right += 1
            
            for i in range(len(temp)):
                nums[low + i] = temp[i]

        mergeSort(nums, 0, len(nums) - 1)
        return nums
