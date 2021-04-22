# Import of data from CSV file

import csv
file = open('small_dataset.csv')
csv_reader = csv.reader(file)
next(csv_reader)
shares = list((row[0], int(row[1]), float(f"{int(row[1])*(1+float(row[2])):.2f}")) for row in csv_reader)

# Brute-force algorithm. Complexity: O(2^n)

def brute_force_search(shares_list, budget, portfolio = []):
    # Base Case : as long as there are shares to screen
    if shares_list:
        # Option 1 : first share of shares_list excluded from portfolio
        portfolio1, portfolio1_profits = brute_force_search(shares_list[1:], budget, portfolio)
        first_share = shares_list[0]
        if first_share[1] <= budget:
            # Option 2: first share of shares_list added to portfolio
            budget = budget - first_share[1]
            portfolio = portfolio + [first_share]
            portfolio2, portfolio2_profits = brute_force_search(shares_list[1:], budget, portfolio)
            # Comparing Option 1 with Option 2
            # Option 2 better than Option 1 : iterate brute_force_search on Option 2
            if portfolio1_profits < portfolio2_profits:
                return portfolio2, portfolio2_profits
        # Option 1 returned as best option
        return portfolio1, portfolio1_profits

    return list(share[0] for share in portfolio), sum(share[2] for share in portfolio) - sum(share[1] for share in portfolio)

if __name__ == "__main__":

    brute_force_portfolio = brute_force_search(shares, budget = 500, portfolio=[])
    print(f"Brute-force portfolio : {brute_force_portfolio}")



