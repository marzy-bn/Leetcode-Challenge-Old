class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hmap = {'a':".-"
         ,'b':"-..."
         ,'c':"-.-."
         ,'d':"-.."
         ,'e':"."
         ,'f':"..-."
         ,'g':"--."
         ,'h':"...."
         ,'i':".."
         ,'j':".---"
         ,'k':"-.-"
         ,'l':".-.."
         ,'m':"--"
         ,'n':"-."
         ,'o':"---"
         ,'p':".--."
         ,'q':"--.-"
         ,'r':".-."
         ,'s':"..."
         ,'t':"-"
         ,'u':"..-"
         ,'v':"...-"
         ,'w':".--"
         ,'x':"-..-"
         ,'y':"-.--"
         ,'z':"--.."}
        trans = set()
        count = 0
        for word in words:
            mapped = ''
            for letter in word:
                mapped += hmap[letter]
            print(mapped)
            if mapped not in trans:
                trans.add(mapped)
                count += 1
        return count