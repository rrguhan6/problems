def fun(prices, fee):
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
        print(cash, hold)
    return(cash)


# fun([1, 3, 7, 5, 10, 3], 3)

fun([1, 3, 2, 8, 4, 9], 2)
