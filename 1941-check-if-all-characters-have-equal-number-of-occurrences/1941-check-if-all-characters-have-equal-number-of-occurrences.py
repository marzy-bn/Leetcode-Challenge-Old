class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hmap = {}
        for char in s:
            if char not in hmap:
                hmap[char] = 1
            else:
                hmap[char] += 1
        check = -1
        for val in hmap.values():
            if check == -1:
                    check = val
            else:
                if check != val:
                    return False
        return True