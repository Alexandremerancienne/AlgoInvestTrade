# Brute force algorithm. Complexity: O(2^n)

import time

def brute_force_search(shares_list, budget, portfolio=[]):
    start = time.time()
    if shares_list:
        # Option 1 : first share of shares_list excluded from portfolio
        portfolio1, portfolio1_profits = brute_force_search(shares_list[1:], budget, portfolio)
        first_share = shares_list[0]

        # Option 2: first share of shares_list added to portfolio
        if first_share[1] <= budget:
            budget = budget - first_share[1]
            portfolio2, portfolio2_profits = brute_force_search(shares_list[1:], budget, portfolio + [first_share])

            # Option 2 returned as the best option
            if portfolio1_profits < portfolio2_profits:
                return portfolio2, portfolio2_profits

        # Option 1 returned as the best option
        return portfolio1, portfolio1_profits
    else:
        return [share[0] for share in portfolio], \
               (float(f"{sum(share[2] for share in portfolio) - sum(share[1] for share in portfolio):.2f}"),
                sum(share[1] for share in portfolio), start)


if __name__ == "__main__":

    # Import of data from CSV file

    import csv
    file = open('small_dataset.csv')
    csv_reader = csv.reader(file)
    next(csv_reader)
    shares = list((row[0], int(row[1]), float(f"{int(row[1]) * (1 + float(row[2])):.2f}")) for row in csv_reader)

    # Application of brute force algorithm

    brute_force_portfolio = brute_force_search(shares, budget=500, portfolio=[])
    print(f"Brute-force portfolio : {brute_force_portfolio[0]}")
    print(f"Portfolio price : {brute_force_portfolio[1][1]}")
    print(f"Portfolio benefits : {brute_force_portfolio[1][0]}")
    print(f"Algorithm executed in : {time.time() - brute_force_portfolio[1][2]}s")
