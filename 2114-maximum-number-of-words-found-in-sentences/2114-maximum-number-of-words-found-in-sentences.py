class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        biggest = 0
        for sentence in sentences:
            spaces = 0
            for ch in sentence:
                if ch == ' ':
                    spaces += 1
            if biggest < spaces:
                biggest = spaces
        return biggest + 1
        
        
        '''
        for sentence in sentences:
            count = 0
            lst = sentence.split()
            if len(lst) > biggest:
                biggest = len(lst)
        return biggest
        '''     