# O(nlogn) time | O(1) space
def nonConstructibleChange(coins):
    coins.sort()
    sum = 0
    for i in range(len(coins)):
        if(coins[i] > (sum + 1)):
            return sum + 1
        sum += coins[i]
    return sum + 1

coins = [5, 7, 1, 1, 2, 3, 22]

print(nonConstructibleChange(coins))
