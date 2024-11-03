import random
import matplotlib.pyplot as plt

def monte_carlo(attempts = 100):
    result = {i: 0 for i in range(2, 13)}
    for _ in range(attempts):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        result[dice_1 + dice_2] += 1

    probability = {}
    for i in range(2, 13):
        probability[i] = result[i]/attempts * 100
    return probability

att = 1000000
probability = monte_carlo(att)
print("Сума\t|\t Ймовірність ")
for key, val in probability.items():
    print(f"{key}\t\t|\t{val:.2f}%")

sums = list(probability.keys())
probabilities = list(probability.values())

plt.figure(figsize=(10, 6))
plt.bar(sums, probabilities, color="skyblue", edgecolor="black")
plt.xlabel("Сума")
plt.ylabel("Ймовірність (%)")
plt.title("Ймовірність сум при киданні двох гральних кубиків")
plt.xticks(range(2, 13))
plt.show()