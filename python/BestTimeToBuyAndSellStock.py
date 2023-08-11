def maxProfit(prices):
    left = 0
    right = 1
    maxProfit = 0
    while right < len(prices):
        currentPrice = prices[right] - prices[left]
        if prices[left] < prices[right]:
            maxProfit = max(maxProfit, currentPrice)
        else:
            left = right
        right += 1
    return maxProfit


print(maxProfit([7,1,5,3,6,4]))