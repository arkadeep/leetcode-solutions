class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left_pointer, right_pointer = 0, (len(numbers) - 1)



        while left_pointer < right_pointer:

            # while numbers[right_pointer] > target and left_pointer < right_pointer:
            #     right_pointer -= 1

            while numbers[left_pointer] + numbers[right_pointer] > target and left_pointer < right_pointer:
                right_pointer -= 1

            while numbers[left_pointer] + numbers[right_pointer] < target and left_pointer < right_pointer:
                left_pointer += 1

            if numbers[left_pointer] + numbers[right_pointer] == target:
                return [left_pointer + 1, right_pointer + 1]