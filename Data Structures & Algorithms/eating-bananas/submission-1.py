class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return math.ceil(max(piles) / (h // len(piles)))
            
            
            
        