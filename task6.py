# Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного
# програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
# Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ —
# назва страви, а значення — це словник з вартістю та калорійністю.


def greedy_algorithm(items, max_sum):
    result = {}
    total_calories = 0
    sorted_items = sorted(items.items(), key=lambda x : x[1]["calories"]/x[1]["cost"], reverse=True)

    for item, val in sorted_items:
        if val["cost"] <= max_sum:
            result[item] = val["cost"]
            max_sum -= val["cost"]
            total_calories += val["calories"]
    return result, total_calories, max_sum


def dp_algorithm(items, max_sum):
    n = len(items)
    dp = [[0] * (max_sum + 1) for _ in range(n + 1)]
    item_list = list(items.keys())

    for i in range(1, n + 1):
        item_name = item_list[i - 1]
        cost = items[item_name]["cost"]
        calories = items[item_name]["calories"]

        for j in range(max_sum + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    # Відновлення списку обраних предметів
    result = {}
    j = max_sum
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name = item_list[i - 1]
            result[item_name] = items[item_name]["calories"]
            j -= items[item_name]["cost"]

    return result, dp[n][max_sum], j

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

select_items, total_calories, amount = greedy_algorithm(items, budget)
print(f"Greedy algorithm:\nselect items: {select_items} \nTotal calories: {total_calories}, amount: {amount}\n\n")

select_items, total_calories, amount  = dp_algorithm(items, budget)
print(f"Dynamic programing:\nselect items: {select_items} \nTotal calories: {total_calories}, amount: {amount}")