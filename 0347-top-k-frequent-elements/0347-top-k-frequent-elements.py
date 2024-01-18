class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        # print(hmap)
        
        #[(1,3),(2,2)(3,1)]
        
        #sorting the dictionary
        sorted_hmap = sorted(hmap.items(), key= lambda x: x[1], reverse=True)
        k_lst = []
        for i in range(k):
            k_lst.append(sorted_hmap[i][0])
        return k_lst