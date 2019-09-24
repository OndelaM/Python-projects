menu = ["sandwiches", "lattes", "cakes", "scones"]

stock = {"sandwiches": 10, "lattes": 50, "cakes": 100, "scones": 250}

prices = {"sandwiches": 30,"lattes": 25, "cakes": 35, "scones": 20}

stock_worth = {k: prices[k]*stock[k] for k in prices}

print(stock_worth)





