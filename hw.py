import timeit


def find_coins_greedy(amount):
  coins = [50, 25, 10, 5, 2, 1]
  result = {}
  for coin in coins:
    count = amount // coin
    if count > 0:
      result[coin] = count
      amount -= count * coin
  return result


def find_min_coins(amount):
  coins = [50, 25, 10, 5, 2, 1]
  dp = [float('inf')] * (amount + 1)
  dp[0] = 0
  used_coins = [{} for _ in range(amount + 1)]

  for i in range(1, amount + 1):
    for coin in coins:
      if i >= coin and dp[i - coin] + 1 < dp[i]:
        dp[i] = dp[i - coin] + 1
        used_coins[i] = used_coins[i - coin].copy()
        used_coins[i][coin] = used_coins[i].get(coin, 0) + 1

  return used_coins[amount]


amount = 113
print("Жадібний алгоритм:", find_coins_greedy(amount))
print("Динамічне програмування:", find_min_coins(amount))

time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
time_dp = timeit.timeit(lambda: find_min_coins(amount), number=1000)
print(f"Час виконання")
print("Жадібний алгоритм:", time_greedy)
print("Динамічне програмування:", time_dp)