class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        count = 0
        out = ''
        for word in s.split():
            out += word
            out += ' '
            count += 1
            if count == k:
                out = out.rstrip()
                return out
        
                
            