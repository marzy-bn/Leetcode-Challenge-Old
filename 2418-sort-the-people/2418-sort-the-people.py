class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hmap = {}
        for name,height in zip(names,heights):
            hmap[height] = name
        
        out = []
        for i in range(0,len(heights)):
            h = 0
            for height,name in hmap.items():
                if h < height:
                    h = height
            out.append(hmap[h])
            del hmap[h]
        return out
            
            