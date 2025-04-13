# Last updated: 4/13/2025, 3:21:12 PM
# Need a better understanding of how to write binary search,
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        print("Nums:", nums)
        print("Target:", target)

        if not nums:
            return -1

        mid_point = int(len(nums) / 2) + 0

        print("midpoint:", mid_point)
        print("Value:", nums[mid_point])

        if target == nums[mid_point]:
            print("target equals midpoint")
            return mid_point
        elif target < nums[mid_point]:
            print("target is lower than the midpoint")
            return self.search(nums[:mid_point], target)
        else:
            print("target is greater than the midpoint")
            result = self.search(nums[mid_point+1:], target)
            if result == -1:
                return -1
            else:
                # Add 1 to skip over the midpoint itself
                return mid_point + 1 + result