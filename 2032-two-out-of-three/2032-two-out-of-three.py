class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        hmap = collections.Counter()
        
        def func(nums):
            for x in set(nums):
                hmap[x] += 1
            print(hmap)
    
        func(nums1)
        func(nums2)
        func(nums3)
        
        out = []
        for x in hmap.keys():
            if hmap[x] >= 2:
                out.append(x)
        return out