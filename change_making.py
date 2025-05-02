from typing import List, Dict


def find_coins_greedy(
    amount: int, coins: List[int] = [50, 25, 10, 5, 2, 1]
) -> Dict[int, int]:
    result: Dict[int, int] = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(
    amount: int, coins: List[int] = [1, 2, 5, 10, 25, 50]
) -> Dict[int, int]:
    min_coins: List[float] = [float("inf")] * (amount + 1)
    min_coins[0] = 0
    last_used: List[int] = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_used[i] = coin

    result: Dict[int, int] = {}
    current = amount
    while current > 0:
        coin = last_used[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


# Example usage:
if __name__ == "__main__":
    amount: int = 113
    print("Greedy result:", find_coins_greedy(amount))
    print("Dynamic programming result:", find_min_coins(amount))
