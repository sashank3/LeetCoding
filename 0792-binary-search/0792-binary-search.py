class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Set 2 pointers for left and right. Start a loop while left <= right
        # If mid point is less than target, l = mid + 1, else r = mid - 1

        l, r = 0, len(nums) - 1

        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1

            


        