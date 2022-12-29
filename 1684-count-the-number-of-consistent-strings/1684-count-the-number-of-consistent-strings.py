class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        print(allowed)
        count = 0
        for word in words:
            for l in word:
                if l not in allowed:
                    count+=1
                    break
        return len(words) - count