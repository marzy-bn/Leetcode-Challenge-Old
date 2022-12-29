import string
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hmap = {}
        alphabet = string.ascii_lowercase
        i = 0
        l = 0
        while i < len(key):
            if key[i] == ' ':
                i += 1
            elif key[i] != ' ':
                if key[i] not in hmap.keys():
                    hmap[key[i]] = alphabet[l]
                    l += 1
                i += 1
        out = ''
        for m in message:
            if m == ' ':
                out += ' '
            else:
                out += hmap[m]
        return out
        
                    
                
                