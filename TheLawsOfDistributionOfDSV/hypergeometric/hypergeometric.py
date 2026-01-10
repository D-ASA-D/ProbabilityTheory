print(f"d) Гипергеометрический закон распределения\n"
      f"На сервер ежедневно поступает 60 HTTP запросов, из них 20 вредоносных.\n"
      f"Все запросы сохраняются в журнал логов.\n"
      f"Ежедневно случайным образом отбирается 13 HTTP запросов для проверки.\n"
      f"Случайная величина X — число вредоносных запросов в выборке за день.")

import scipy
from prettytable import PrettyTable
from math import sqrt
import matplotlib.pyplot as plt

N = 60
M = 20
n = 13

xMax = min(n, M)
xValues = list(range(0, xMax + 1))

print(f"N = {N} (общее количество запросов)")
print(f"M = {M} (количество вредоносных запросов)")
print(f"n = {n} (объем выборки)\n")
print(f"X = 0, 1, 2, ..., m, ..., {xMax}")
print(f"где m = 0, 1, 2, ..., min(n, M) = min({n}, {M}) = {xMax}")

tableHyper = PrettyTable()
fieldNames = ["X"] + [str(x) for x in xValues]
tableHyper.field_names = fieldNames

row = ["P(X)"]
probabilities = []
for x in xValues:
    prob = (scipy.special.comb(M, x) * scipy.special.comb(N - M, n - x) / scipy.special.comb(N, n))
    probabilities.append(prob)
    row.append(f"{prob:.9f}")

tableHyper.add_row(row)
print("\nЗакон распределения:")
print(tableHyper)

print("P(X = m) = C(M,m) * C(N-M, n-m) / C(N,n)")
print(f"где m = 0, 1, 2, ..., min(n, M) = {xMax}")
print(f"Проверка: sum(P(X)) = {sum(probabilities):.12f} = 1")

mHyper = n * (M / N)
print(f"M(X) = n * (M/N) = {n} * ({M}/{N}) = {mHyper:.4f}")

dHyper = n * (M/(N-1)) * (1 - M/N) * (1 - n/N)
print(f"D(X) = n * M/(N-1) * (1 - M/N) * (1 - n/N)  = {n} * {M}/({N}-1) * (1 - {M}/{N}) * (1 - {n}/{N}) = {n} * {M/(N-1):.4f} * {1-M/N:.4f} * {1-n/N:.4f} = {dHyper:.6f}" )

sigma_hyper = sqrt(dHyper)
print(f"Sigma(X) = sqrt(D(X)) = sqrt({dHyper:.6f}) = {sigma_hyper:.4f}")

dictV = {}
for x in xValues:
    dictV[x] = scipy.special.comb(M, x) * scipy.special.comb(N - M, n - x) / scipy.special.comb(N, n)
maxValues = max(dictV.values())

maxKeys = [key for key, value in dictV.items() if value == maxValues]
print(f'Mo(X) = ', end='')
for el in maxKeys:
    print(el, end=' ')

plt.figure(figsize=(10, 5))
plt.plot(xValues, probabilities, 'mo-', linewidth=2, markersize=8, markerfacecolor='white')
plt.title(f'Гипергеометрическое распределение: (N={N}, M={M}, n={n})')
plt.xlabel('X = 0, 1, 2, ..., m, ..., min(n, M)')
plt.ylabel('P(X) = C(M,m) * C(N-M, n-m) / C(N,n)')
plt.grid(True, alpha=0.3)
plt.xticks(xValues)

for x, prob in zip(xValues, probabilities):
    plt.text(x, prob + 0.01, f'{prob:.8f}', ha='center', fontsize=9)
plt.show()
