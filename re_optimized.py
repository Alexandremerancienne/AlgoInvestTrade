# New optimized algorithm - Complexity: O(n*logn)

import time

def re_optimized_search(shares_list, budget):
    start = time.time()
    optimized_portfolio = []
    shares_list.sort(key = lambda share:share[1]/share[2])
    total_profit = 0
    for share in shares_list:
        share_price = float(share[1])
        share_profit = float(share[2])
        if budget - share_price >= 0:
            budget -= share_price
            total_profit += share_profit
            optimized_portfolio.append(share)
        else:
            budget -= 0
            total_profit += 0

    return list(share[0] for share in optimized_portfolio), \
           (float(f"{sum(share[2] for share in optimized_portfolio) - sum(share[1] for share in optimized_portfolio):.2f}"),
            f"{sum(share[1] for share in optimized_portfolio):.2f}", start)

if __name__ == "__main__":

    # Import of data from CSV file

    import csv
    file = open('dataset1.csv')
    csv_reader = csv.reader(file)
    next(csv_reader)
    shares = list((row[0], float(row[1]), float(f"{float(row[1]) * (1 + float(row[2])/100):.2f}"))
                  for row in csv_reader if float(row[1])>0.0 and float(row[2])>0.0)

    # Application of optimized algorithm

    re_optimized_portfolio = re_optimized_search(shares, 500)
    print(f"Optimized portfolio : {re_optimized_portfolio[0]}")
    print(f"Portfolio price : {re_optimized_portfolio[1][1]}")
    print(f"Portfolio benefits : {re_optimized_portfolio[1][0]}")
    print(f"Algorithm executed in : {time.time() - re_optimized_portfolio[1][2]}s")
