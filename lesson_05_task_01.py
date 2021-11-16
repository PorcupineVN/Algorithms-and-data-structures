# Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа
# должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
import statistics

print('Введите количество предприятий')
n_company = int(input())
company = {}
total_profit = 0

for i in range(1, n_company + 1):
    print(f'Введите название предприятия №{i}')
    name = input()
    profit = []
    for j in range(1, 5):
        print(f'Введите прибыль {name} за {j} квартал')
        profit.append(float(input()))
    profit.append(statistics.mean(profit))
    company[name] = profit
    total_profit += sum(company[name][:4])
avg_profit = total_profit / n_company
print(f'Средняя прибыль всех предприятий за год: {avg_profit}')
low_profit = []
high_profit = []
for key, value in company.items():
    if value[4] < avg_profit:
        low_profit.append(key)
    elif value[4] > avg_profit:
        high_profit.append(key)
print(f'Предприятия, чья прибыль выше среднего: {high_profit}')
print(f'Предприятия, чья прибыль ниже среднего: {low_profit}')
