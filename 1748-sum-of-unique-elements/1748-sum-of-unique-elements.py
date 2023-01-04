class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        Uset = set()
        hset = set()
        for num in nums:
            if num not in Uset and num not in hset:
                Uset.add(num)
            elif num in Uset and num not in hset:
                Uset.remove(num)
                hset.add(num)
        total = 0
        for num in Uset:
            total += num
        return total
            
                
        