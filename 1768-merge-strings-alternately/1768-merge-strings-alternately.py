class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for l1,l2 in zip(word1,word2):
            output += l1
            output += l2
        print(output)
    
        if len(word1) <= len(word2):
            return output + word2[len(word1):len(word2)]
        else:
            return output + word1[len(word2):len(word1)]
            