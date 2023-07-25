class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for element in nums:
            if element not in hset:
                hset.add(element)
            else:
                return True
        return False