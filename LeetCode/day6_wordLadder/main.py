from collections import defaultdict


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList:[str]) -> int:
        wordList.append(beginWord)
        L = len(wordList)
        k = len(beginWord)

        if not endWord or not beginWord:
            return 0

        if endWord not in wordList:
            return 0

        d = defaultdict(list)
        visited = {}
        # pre-work, set up graph with wildcard letter word
        for i in range(L):
            w = wordList[i]
            visited[w] = False
            for j in range(k):
                wildCardWord = w[:j] + '*' + w[j + 1:]
                d[wildCardWord].append(w)

                # perform BFS
        q = [(beginWord, 1)]
        visited[beginWord] = True
        while len(q) != 0:
            currWord, currCount = q[0]
            q.pop(0)

            if currWord == endWord:
                return currCount

            for i in range(k):
                wildCardWord = currWord[:i] + '*' + currWord[i + 1:]

                for neighbor in d[wildCardWord]:
                    if not visited[neighbor]:
                        q.append((neighbor, currCount + 1))
                        visited[neighbor] = True

        return 0

