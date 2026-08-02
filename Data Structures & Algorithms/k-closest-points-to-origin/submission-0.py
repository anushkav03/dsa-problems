class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(xi, yi):
            return math.sqrt(xi^2 - yi^2)
        
        pq = []
        heapq.heapify(pq)
        # push as tuple (key, original data pt)
        for point in points:
            eu_dist = dist(point[0], point[1])
            heapq.heappush(pq, (eu_dist, point))

        closest_k = []
        for _ in range(k):
            val = pq.pop()
            closest_k.append(val[1])

        return closest_k
        