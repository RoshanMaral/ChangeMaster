# ------------------------------
# Greedy Coin Change (AI Heuristic)
# ------------------------------
def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result if amount == 0 else None


# ------------------------------
# Dynamic Programming (Optimal)
# ------------------------------
def dp_coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)  # to reconstruct solution

    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0 and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
                parent[a] = coin

    if dp[amount] == float("inf"):
        return None  # no solution

    # reconstruct solution
    res = []
    a = amount
    while a > 0:
        res.append(parent[a])
        a -= parent[a]
    return res


# ------------------------------
# Main Program (User inputs amount)
# ------------------------------
if __name__ == "__main__":
    # Fixed coin denominations
    coins = [1, 2, 5, 10]

    # Take only amount as input
    amount = int(input("Enter the amount: "))

    greedy_result = greedy_coin_change(coins[:], amount)  # copy list since greedy sorts
    dp_result = dp_coin_change(coins, amount)

    print("\nAvailable coins:", coins)
    print("Target amount:", amount, "\n")

    if greedy_result:
        print("Greedy Algorithm result:", greedy_result, " (coins used:", len(greedy_result), ")")
    else:
        print("Greedy Algorithm result: No solution")

    if dp_result:
        print("DP Optimal result:     ", dp_result, " (coins used:", len(dp_result), ")")
    else:
        print("DP Optimal result: No solution")
