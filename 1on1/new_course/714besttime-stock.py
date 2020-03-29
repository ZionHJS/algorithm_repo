class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        bs = [0 for i in range(2*len(prices))]
        for i in range(len(bs)):
            if i % 2 == 0:  # buy
                bs[i] = -prices[0] - i//2*fee
            else:  # sell
                bs[i] = -i//2*fee

        for i in range(1, len(prices)):
            bs[0] = max(bs[0], -prices[i])
            # for buys
            for j in range(2, 2*(i+1), 2):
                bs[j] = max(bs[j-1]-prices[i], bs[j])
            # for sells
            for j in range(1, 2*(i+1), 2):
                bs[j] = max(bs[j-1]+prices[i]-fee, bs[j])

        #print("bs:", bs)
        return max(bs) if max(bs) > 0 else 0
