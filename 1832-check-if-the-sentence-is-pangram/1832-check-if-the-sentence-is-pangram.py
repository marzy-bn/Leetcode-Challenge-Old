class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        import string
        alphabet = list(string.ascii_lowercase)
        hset = set(sentence)
        seen = set()

        for i,letter in enumerate(alphabet):
            if letter not in hset:
                return False
            if letter in seen:
                return False
            if letter in hset:
                seen.add(letter)
        return True
            