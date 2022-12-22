class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tpls = sorted(zip(heights,names), reverse=True)
        out = []
        for a,b in tpls:
            out.append(b)
        return out
            