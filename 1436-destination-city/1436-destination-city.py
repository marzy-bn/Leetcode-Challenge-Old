class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = collections.defaultdict(int)
        for A,B in paths:
            s[A] += 1
            s[B] += 0
        print(s)
        for x in s.keys():
            if s[x] == 0:
                return x
        return ''
            
        
            
                
        
                