# Optimized algorithm - Complexity: O(Wn), W being the constraint

import time

def optimized_search(budget, shares_list):
    start = time.time()

    # Matrix of the maximum number of shares obtainable for every sub-budget
    matrix = [[0 for x in range(budget+1)] for x in range(len(shares_list)+1)]

    for i in range(1, len(shares_list)+1):
        for w in range(1, budget+1):
            if shares_list[i-1][1] <= w:
                matrix[i][w] = max(shares_list[i-1][2]+matrix[i-1][w-shares_list[i-1][1]], matrix[i-1][w])
            else:
                matrix[i][w] = matrix[i-1][w]

    # Return best equity portfolio
    k = budget
    n = len(shares_list)
    optimized_portfolio = []

    while k >=0 and n>=0:
        previous_share = shares_list[n-1]
        if matrix[n][k] == matrix[n-1][k-previous_share[1]]+ previous_share[2]:
            optimized_portfolio.append(previous_share)
            k -= previous_share[1]
        n -=1

    return list(share[0] for share in optimized_portfolio), \
           (float(f"{sum(share[2] for share in optimized_portfolio) - sum(share[1] for share in optimized_portfolio):.2f}"),
            sum(share[1] for share in optimized_portfolio), start)

if __name__ == "__main__":

    # Import of data from CSV file

    import csv
    file = open('small_dataset.csv')
    csv_reader = csv.reader(file)
    next(csv_reader)
    shares = list((row[0], int(row[1]), float(f"{int(row[1]) * (1 + float(row[2])):.2f}")) for row in csv_reader)

    # Application of optimized algorithm

    optimized_portfolio = optimized_search(500, shares)
    print(f"Optimized portfolio : {optimized_portfolio[0]}")
    print(f"Portfolio price : {optimized_portfolio[1][1]}")
    print(f"Portfolio benefits : {optimized_portfolio[1][0]}")
    print(f"Algorithm executed in : {time.time() - optimized_portfolio[1][2]}s")
