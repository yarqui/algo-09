# Greedy vs Dynamic Programming

This README analyses and compares the performance of two algorithms implemented to solve the change-making problem using a coin set `[50, 25, 10, 5, 2, 1]`.

---

## Algorithms Implemented

1. **Greedy Algorithm (`find_coins_greedy`)**
   - Strategy: Always chooses the largest possible coin first.
   - Time Complexity: **O(k)**, where `k` is the number of coin denominations.
   - Characteristics: Very fast and efficient, but **may not always produce an optimal solution** for arbitrary coin sets.

2. **Dynamic Programming Algorithm (`find_min_coins`)**
   - Strategy: Builds up the solution by computing the minimum number of coins needed for every amount from `1` to `N`.
   - Time Complexity: **O(N × k)**, where `N` is the amount and `k` is the number of coin types.
   - Characteristics: **Always produces the optimal (minimal) number of coins**, but uses more time and memory.

---

## Performance Comparison

### Greedy Algorithm
**Pros**:
  - Extremely fast and simple to implement.
  - Performs well with canonical coin systems like [50, 25, 10, 5, 2, 1].

**Cons**:
  - Fails to guarantee optimality with non-standard coin sets (e.g., [1, 3, 4]).

### Dynamic Programming
**Pros**:
  - Always finds the minimal number of coins for **any** coin set.
  
**Cons**:
  - Slower, especially for large amounts (e.g., 10,000+), due to time and space complexity.

---

## Conclusion

- For typical cash register systems using standard coin denominations, the **greedy algorithm is preferred** due to its speed and simplicity.
- If the coin set is irregular or optimality is critical, the **dynamic programming algorithm is more reliable** despite the heavier computational cost.
- Overall, **greedy is more efficient for large sums** in practical scenarios with canonical coins, while **dynamic programming is more robust**.