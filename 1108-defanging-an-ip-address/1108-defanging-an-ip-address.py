class Solution:
    def defangIPaddr(self, address: str) -> str:
        output = ""
        for num in address:
            if num != '.':
                output += num
            else:
                output += '[.]'
        return output