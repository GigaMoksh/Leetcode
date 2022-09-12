class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        i, j = 0, len(tokens)
        while i < j:
            if power >= tokens[i]:
                power -= tokens[i]
                i += 1
            elif i - (n - j) and j > i + 1:
                j -= 1
                power += tokens[j]
            else:
                break
        return i - (n - j)
    
