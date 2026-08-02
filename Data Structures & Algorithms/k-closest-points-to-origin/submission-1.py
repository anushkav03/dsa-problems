class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eu_dist(xi, yi):
            return xi**2 + yi**2
        
        pq = []
        heapq.heapify(pq)
        # push as tuple (key, original data pt)
        for point in points:
            dist = eu_dist(point[0], point[1])
            heapq.heappush(pq, (dist, point))

        closest_k = []
        for _ in range(k):
            val = heapq.heappop(pq)
            closest_k.append(val[1])

        return closest_k
        