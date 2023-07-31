class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for val in nums:
            if val not in hset:
                hset.add(val)
            else:
                return True
        return False