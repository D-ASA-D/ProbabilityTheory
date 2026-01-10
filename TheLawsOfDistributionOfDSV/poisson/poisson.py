print(f"b) Закон распределения Пуассона\n"
      f"На сервер в среднем поступает 18 http запросов за 90 минут.\n"
      f"Случайная величина X - число запросов за 10 минут.")
lambdaPoisson = 18/90 * 10

import scipy
from math import sqrt, exp
import matplotlib.pyplot as plt

probsPoisson = []
max_m = 10

for k in range(max_m + 1):
    prob = (exp(-lambdaPoisson) * (lambdaPoisson**k)) / scipy.special.factorial(k)
    probsPoisson.append(prob)

print("\nЗакон распределения:")
print("-"*67)
print(f"|  X  |    0     |    1     |    2     |  ...  |    {max_m}    |  ...  |")
print("-"*67)
print("| P(X)|", end="")

for k in range(3):
    print(f" {probsPoisson[k]:.6f} |", end="")

print("  ...  |", end="")

print(f" {probsPoisson[max_m]:.6f} |", end="")

print("  ...  |")
print("-"*67)
print()
print("-"*81)
print(f"|  X  |   0    |     1      |        2        |  ...  |        m        |  ...  |")
print("-"*81)
print("| P(X)|", end="")
print(f" e^(-λ) | λ * e^(-λ) | (λ^2)/2!*e^(-λ) |  ...  | (λ^m)/m!*e^(-λ) |  ...  |")
print("-"*81)

print(f"где λ = {lambdaPoisson}")

poissonSumPy = sum(probsPoisson)
print(f"Сумма вероятностей: sum(P(X)) = {poissonSumPy:.10f} = 1")

print(f"M(X) = λ = {lambdaPoisson}")
print(f"D(X) = λ = {lambdaPoisson}")
print(f"Sigma(X) = sqrt(λ) = sqrt({lambdaPoisson}) = {sqrt(lambdaPoisson):.6f}")

dictV = {}
for m in range(max_m + 1):
    dictV[m] = (exp(-lambdaPoisson) * (lambdaPoisson**m)) / scipy.special.factorial(m)
maxValues = max(dictV.values())

maxKeys = [key for key, value in dictV.items() if value == maxValues]
print(f'Mo(X) = ', end='')
for el in maxKeys:
    print(el, end=' ')
xValues = list(range(max_m + 1))
plt.figure(figsize=(10, 5))
plt.plot(xValues, probsPoisson, 'ro-', linewidth=2, markersize=8)
plt.title(f'Распределение Пуассона: λ={lambdaPoisson}')
plt.xlabel('X - число запросов за 10 минут')
plt.ylabel('P(X) - вероятность')
plt.grid(True, alpha=0.3)
plt.xticks(xValues)

for x, y in zip(xValues, probsPoisson):
    plt.text(x, y + 0.01, f'{y:.6f}', ha='center', fontsize=9)
plt.show()
