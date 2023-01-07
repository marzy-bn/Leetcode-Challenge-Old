class Solution:
    def checkString(self, s: str) -> bool:
        flag = 'a'
        for char in s:
            if char == 'b' and flag == 'a':
                flag = 'b'
            elif flag == 'b' and char == 'a':
                return False
        return True
            