class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        i = 0
        output = 0
        while i<len(accounts):
            j = 0
            total = 0
            while j < len(accounts[i]):
                total += accounts[i][j]
                j += 1
            if total > output:
                output = total
            i+= 1
        return output
        