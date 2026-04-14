class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums, i, j):
            if i >= j:
                return
            mid = (i + j) // 2
            mergeSort(nums, i, mid)
            mergeSort(nums, mid + 1, j)
            merge(nums, i, mid, j)

        def merge(nums, i, mid, j):
            left = i
            right = mid + 1
            temp = list()
            while left <= mid and right <= j:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            while left <= mid:
                temp.append(nums[left])
                left += 1
            while right <= j:
                temp.append(nums[right])
                right += 1
            for index in range(len(temp)):
                nums[i + index] = temp[index]
   
        mergeSort(nums, 0, len(nums) - 1)
        return nums