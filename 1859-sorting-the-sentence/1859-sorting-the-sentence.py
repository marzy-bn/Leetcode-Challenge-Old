class Solution:
    def sortSentence(self, s: str) -> str:
        hmap = {}
        for sentence in s.split():
            hmap[int(sentence[-1])] = sentence[:-1]
        out = ""
        for num in range(1,len(s.split())+1):
            out += hmap[num]
            out += ' '
        out = out.rstrip()
        return out
        