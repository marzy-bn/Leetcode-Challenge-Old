import string
class Solution:
    def generateTheString(self, n: int) -> str:
        lst = string.ascii_lowercase
        st1 = random.choice(lst)
        
        if n == 1:
            return st1
        if n % 2 == 0:
            for ch in lst:
                if ch != st1:
                    st2 = ch
            return st1 + (n-1) * st2
        else:
            for ch in lst:
                if ch != st1:
                    st2 = ch
            for ch in lst:
                if ch != st1 and ch != st2:
                    st3 = ch
            return st1 + st2 + st3 * (n-2)
                
            
            