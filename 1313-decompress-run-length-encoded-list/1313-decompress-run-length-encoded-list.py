class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i,num in enumerate(nums):
            if i%2==0:
                freq = num
            else:
                val = num
                output += freq * [val]
        return output
            