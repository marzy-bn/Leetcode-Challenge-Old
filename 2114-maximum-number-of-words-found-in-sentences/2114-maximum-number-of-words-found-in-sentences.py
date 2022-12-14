class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        biggest = 0
        for sentence in sentences:
            count = 0
            lst = sentence.split()
            if len(lst) > biggest:
                biggest = len(lst)
        return biggest
                