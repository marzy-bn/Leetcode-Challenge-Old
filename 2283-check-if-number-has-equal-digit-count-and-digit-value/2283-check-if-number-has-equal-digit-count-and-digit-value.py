class Solution:
    def digitCount(self, num: str) -> bool:
        hmap = {}
        for item in num:
            if item not in hmap:
                hmap[item] = 1
            else:
                hmap[item] += 1
        hmap2 = {}
        for idx,val in enumerate(num):
            if val != str(0):
                hmap2[str(idx)] = int(val)
        print(hmap)
        print(hmap2)
        return hmap == hmap2