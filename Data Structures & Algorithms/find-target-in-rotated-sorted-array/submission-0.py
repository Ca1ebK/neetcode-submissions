class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            else:
                # left half is sorted
                if nums[left] <= nums[mid]:
                    # target is in sorted left half
                    if target >= nums[left] and target < nums[mid]:
                        right = mid - 1
                    # target is in unsorted right half
                    else:
                        left = mid + 1
                # right half is sorted
                else:
                    # if target is in the right sorted half
                    if target > nums[mid] and target <= nums[right]:
                        left = mid + 1
                    # target is in the unsorted left half
                    else:
                        right = mid -1
            
        return -1