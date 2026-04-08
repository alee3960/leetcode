from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {} # key: number, value: index
        for i, num in enumerate(nums):
            c = target - num # the complement should be equal to the other number

            # check if we've already seen the other number
            if c in h:
                return [h[c], i] # return both indeces
            
            # add the number (which the compliment to the next number) and the index
            h[num] = i 
        return []
