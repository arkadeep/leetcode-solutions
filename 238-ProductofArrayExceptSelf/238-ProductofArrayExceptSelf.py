class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # Creating the most optimal solution, which involves just the output list

        result_list = []

        len_input = len(nums)

        # First pass - create the prefixes

        pre_num = 1

        for i in range(len_input):
            
            result_list.append(pre_num)

            pre_num = pre_num * nums[i]

        print(result_list)

        # Second pass - create the suffixes, need to go from left to right

        suff_num = 1

        for i in range(len_input, 0, -1):
            
            result_list[i - 1] = result_list[i - 1] * suff_num 

            suff_num = suff_num * nums[i - 1]

        print(result_list)

        return result_list