#******************************************************************************
# barrier.py
#******************************************************************************
# Name: Abrar Alsayedi
#******************************************************************************
# Remarks (optional):
#
#
#

iimport random

total_money = 0
wins = 0

for _ in range(1000000):
    x1 = random.randint(50, 70)
    x2 = random.randint(50, 70)
    x3 = random.randint(50, 70)

    winnings = 0

    if x1 < 65 and x2 < 65 and x3 < 65 and x3 > 55:
        winnings = x3 - 55

    total_money += winnings

    if winnings >= 1:
        wins += 1

average = total_money / 1000000
probability = wins / 1000000

print(f"AVERAGE: {average:.6f}")
print(f"PROBABILITY: {probability:.6f}")

