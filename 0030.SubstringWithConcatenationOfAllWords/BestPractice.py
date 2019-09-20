class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or len(s) < len(words[0]):
            return []
        wordCount = {}
        for w in words:
            if w in wordCount:
                wordCount[w] += 1
            else:
                wordCount[w] = 1
        l = len(words[0])
        window = l * len(words)
        output = []
        for i in range(l):
            index = i
            while index + window <= len(s):
                memo = dict(wordCount)
                endIndex = index + window
                shouldBreak = False
                while endIndex > index:
                    w = s[endIndex-l:endIndex]
                    if not w in memo or memo[w] <= 0:
                        shouldBreak = True
                        break
                    memo[w] -= 1
                    endIndex -= l
                if shouldBreak:
                    index = endIndex
                    continue
                output.append(index)
                index += l
        return output