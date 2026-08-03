class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid_k(piles, h, k):
            time = sum([math.ceil(pile/k) for pile in piles])
            return time <= h

        # upper bound value for k
        ub = math.ceil(max(piles) / (h // len(piles)))
        lb = 1
        smallest_k = ub

        # do binary search
        target_k = ub
        while ub >= lb:
            target_k = ((ub - lb) // 2) + lb
            if valid_k(piles, h, target_k):
                smallest_k = target_k
                ub = target_k - 1
            else:
                lb = target_k + 1

        return smallest_k
            
            
            
        