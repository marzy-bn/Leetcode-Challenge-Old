class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        hmap = {'--X':-1,'X--':-1,'X++':+1,'++X':+1}
        total = 0
        for op in operations:
            total = total + hmap[op]
        return total