from sys import stdin

Inf = 1000000000


def min_coins_greedy(coins, value):
    rest, check, coin_indeks, result = value, 0, 0, 0
    while check != value: # Trengs egentlig dette? Fiks opp
        antall_ganger, rest = rest//coins[coin_indeks], rest%coins[coin_indeks]
        if rest == 0:
            result += antall_ganger
            return result
        elif antall_ganger > 0:
            check += antall_ganger * coins[coin_indeks]
            result  += antall_ganger
            coin_indeks += 1
        else:
            coin_indeks += 1
    return result


def min_coins_dynamic(coins, value):
    #Lær dynamisk
    pass

def can_use_greedy(coins):
    for i in range(len(coins)-1):
        if (coins[i] // coins[i+1]) < 2:
            return False
    return True

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line)))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line)))
