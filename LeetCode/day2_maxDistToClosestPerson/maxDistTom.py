class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        L = len(seats)
        # Edge case: only 2 seats
        if L == 2:
            if seats[0] == 0:
                return 1
            else:
                return 0
        maxDist = -1;
        hasSeenOne = False
        start = 0 if seats[0] == 0 else -1
        for i in range(L):
            if ((seats[i] == 1) and (start != -1)):
                if hasSeenOne:
                    w = i - start
                    if w % 2 == 0:
                        dist = (w // 2)
                    else:
                        dist = (w // 2) + 1
                else:
                    dist = i
                maxDist = max(maxDist, dist)
                start = -1
            elif seats[i] == 0 and start == -1:
                start = i
            if seats[i] == 1:
                hasSeenOne = True

                # Edge case:  IF the last stride was not finished
        if start != -1:
            dist = L - start
            maxDist = max(dist, maxDist)

        # Edge case: There is only 1 available seat
        if maxDist == -1:
            return 1

        return maxDist
