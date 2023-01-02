class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        tcount = 0
        for num in nums:
            count = 0
            while num // 10 != 0:
                num = num // 10
                count += 1
            if (count + 1) % 2 == 0:
                tcount += 1
        return tcount