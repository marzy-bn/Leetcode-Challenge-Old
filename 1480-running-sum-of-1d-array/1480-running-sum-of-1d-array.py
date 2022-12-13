class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        output = []
        for num in nums:
            total = total + num
            output.append(total)
        return output            