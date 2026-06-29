class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_num = {}
        for i,num in enumerate(nums):
            compliment= target -num
            if compliment in map_num:
                return [map_num[compliment], i]
            map_num[num] = i