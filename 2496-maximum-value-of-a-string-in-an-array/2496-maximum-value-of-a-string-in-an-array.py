class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        vals = set()
        for item in strs:
            flag = 0
            for l in item:
                if l.isdigit() == False:
                    flag = 1
                    vals.add(len(item))
                    break
            if flag == 0:
                vals.add(int(item))
        return max(vals)   
        