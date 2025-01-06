class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
        
        # nums.sort()

        # result = []

        # length = len(nums)

        # # print("List:", nums)

        # for ix in range(length):
            
        #     # Since the list is sorted, once we have a positive anchor, it is impossible
        #     # to get a sum of 0, since all numbers which will come after will also be positive
        #     if nums[ix] > 0:
        #         break

        #     if ix > 0 and nums[ix] == nums[ix - 1]:
        #         continue

        #     left = ix + 1
        #     right = length - 1

        #     # print("Current anchor index:", nums[ix])

        #     while left < right: 
                
        #         # print("Starting left index: ", nums[left])
        #         # print("Starting right index: ", nums[right])

        #         while left < (right) and nums[ix] + nums[left] + nums[right] > 0:

        #             right -= 1

        #             # print("Sum is greater than 0, reducing right index")
        #             # print(f"Left: {left}, Right: {right}")
        #             # print("Updated right index", nums[right])

        #         while left < right and nums[ix] + nums[left] + nums[right] < 0:

        #             left += 1

        #             # print("Sum is less than 0, increasing left index")
        #             # print(f"Left: {left}, Right: {right}")
        #             # print("Updated left index", nums[left])

        #         if nums[ix] + nums[left] + nums[right] == 0 and left < right:

        #             # print("Sum is 0")
        #             # print(f"Anchor: {nums[ix]}, left: {nums[left]}, right: {nums[right]}")
        #             # print(f"Inserting: {[nums[ix], nums[left], nums[right]]}")
        #             result.append([nums[ix], nums[left], nums[right]])
        #             left += 1
        #             right -= 1
        #         # else:
        #         #     left += 1
        #         #     right -= 1
        
        # a = []

        # for l in result:
        #     if l not in a:
        #         a.append(l)

        # return a
        