class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        ## naive method, use set
        # bull, cow = 0, 0
        # indexS = {}  # num : ste([index])
        # for idx, d in enumerate(secret):
        #     if not d in indexS:
        #         indexS[d] = set([idx])
        #     else:
        #         indexS[d].add(idx)
        # indexG = {}
        # for idx, d in enumerate(guess):
        #     if not d in indexG:
        #         indexG[d] = set([idx])
        #     else:
        #         indexG[d].add(idx)
        # for d in indexS:
        #     if d in indexG:
        #         inter = indexS[d].intersection(indexG[d])
        #         bull += len(inter)
        #         indexS[d] -= inter
        #         indexG[d] -= inter
        #         cow += min(len(indexS[d]), len(indexG[d]))
        # return str(bull)+"A"+str(cow)+"B"
        
        ## one pass method, tricky
        bull, cow = 0, 0
        num = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if num[int(secret[i])] < 0:  # guess visit this number
                    cow += 1
                if num[int(guess[i])] > 0:  # secret visit this number
                    cow += 1
                num[int(secret[i])] += 1
                num[int(guess[i])] -= 1  # reset 
        return str(bull)+"A"+str(cow)+"B"
