class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for val in s:
            if stack and stack[-1]==val:
                stack.pop()
            else:
                stack.append(val)
        out = ""
        for el in stack:
            out += el
        return out