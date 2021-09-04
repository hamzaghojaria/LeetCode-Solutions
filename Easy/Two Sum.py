class Solution:
    from typing import List
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # List to store results
        result = []
    # Dictionary to store the difference and its index
        index_map = {}
    # Loop for each element
        for i, n in enumerate(nums):
            # Difference which needs to be checked
            difference = target - n
            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = i
        return result                          
      
      
      
      OR
      
      class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num1 + num2 == target:
                    return [i, j+i+1]
