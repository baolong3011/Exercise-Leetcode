class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0
        while num1 and num2:
            if num1 >= num2:
                num1 = num1 - num2
                operations += 1
            elif num1 <= num2:
                num2 = num2 - num1
                operations += 1
            if num1 == 0 or num2 == 0:
                return operations
        return operations