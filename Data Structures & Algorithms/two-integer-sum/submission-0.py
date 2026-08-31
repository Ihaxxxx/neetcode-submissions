class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = i

            difference = target - nums[i]
            if difference in map and i != map[difference]:
                return [map[difference],i]