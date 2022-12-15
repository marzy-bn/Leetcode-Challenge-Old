class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hmap = {}
        for letter,digit in zip(s,indices):
            hmap[digit] = letter
        output = ""
        i = 0
        while i < len(hmap):
            output += hmap[i]
            i += 1
        return output