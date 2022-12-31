class Solution:
    def freqAlphabets(self, s: str) -> str:
        hmap = {}
        num = 1
        asc = 97
        while num >= 1 and num <= 9:
            hmap[str(num)] = chr(asc)
            num += 1
            asc += 1
        num = 10
        asc = 106
        while num >= 10 and num <= 26:
            hmap[str(num)+'#'] = chr(asc)
            num += 1
            asc += 1
        idx = len(s) - 1
        out = ''
        while idx >= 0:
            if s[idx] == '#':
                out = hmap[s[idx-2:idx+1]] + out
                idx -= 3
            else:
                out = hmap[s[idx]] + out
                idx -= 1
        return out
                
                
            
        
        
        
        