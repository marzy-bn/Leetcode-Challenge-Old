class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for i in range(len(nums)+1)]
        
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        # print(hmap)
        
        #[(1,3),(2,2)(3,1)]
        
        for key,val in hmap.items():
            freq[val].append(key)
        
        output = []
        for i in range(len(freq)-1,0,-1):
            for item in freq[i]:
                output.append(item)
                if len(output) == k:
                    return output