class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        total1 = ''
        for word in word1:
            total1 += word
        
        total2 = ''
        for word in word2:
            total2 += word
        
        return total1 == total2
        