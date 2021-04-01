class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = len(s)
        if L == 0 or L == 1:
            return L

        currStringStart = currLength = maxLength = 0
        lookup = {}

        # init lookup table
        for i in range(32, 127):
            c = chr(i)
            lookup[c] = -1

        for i in range(L):
            k = s[i]
            v = lookup[k]
            if v != -1:
                maxLength = currLength if currLength > maxLength else maxLength
                end = lookup[k] + 1

                for j in range(currStringStart, end):
                    kk = s[j]
                    lookup[kk] = -1  # set all indices from currStringStart to i to -1
                    currLength -= 1  # decrement length

                currStringStart = end

            lookup[k] = i
            currLength += 1

        maxLength = currLength if currLength > maxLength else maxLength

        return maxLength

