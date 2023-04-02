def buyAndSell(prices):
    buyPrice = 2147483647
    maxProfit = 0
    profit = 0

    for i in range(0,len(prices)):
        if buyPrice<prices[i]:
            profit = prices[i]-buyPrice
            maxProfit = max(profit,maxProfit)
        else:
            buyPrice = prices[i]
        

    return maxProfit

# ---------------------------------------------------------

prices = [7,1,5,3,6,4]
Profit = buyAndSell(prices)
print("The maximum Profit = ",Profit)