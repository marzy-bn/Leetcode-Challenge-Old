class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hset = set()
        for letter in jewels:
            hset.add(letter)
        count = 0
        for ele in stones:
            if ele in hset:
                count += 1
        return count