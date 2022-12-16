class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        i = 0
        output = 0
        while i<len(accounts):
            total = 0
            total = sum(accounts[i])
            if total > output:
                output = total
            i+= 1
        return output
        