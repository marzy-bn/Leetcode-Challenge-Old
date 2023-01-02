class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        out = [start]
        for g in gain:
            out.append(start + g)
            start = start + g
        
        for idx,item in enumerate(out):
            if idx == 0:
                high = item
            else:
                if item > high:
                    high = item
        return high
                    
            