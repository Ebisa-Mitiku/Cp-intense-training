class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        index=0
        for i in range(len(heights)):
            if(heights[i]!=expected[i]):
                index+=1
        return(index)
