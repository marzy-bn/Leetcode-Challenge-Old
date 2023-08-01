from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {']':'[','}':'{',')':'('}
        
        stack = deque()
        for val in s:
            if val in hmap.keys():
                if stack and stack[-1] == hmap[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        
        if len(stack) == 0:
            return True
        return False