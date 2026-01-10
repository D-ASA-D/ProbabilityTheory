print(f"a)Биномиальный закон распределения\n"
      f"Футболист бьет пенальти с вероятностью забить 0.3.\n"
      f"За матч происходит 10 пенальти. X - число забитых мячей.")

import scipy
from prettytable import PrettyTable
from math import sqrt
import matplotlib.pyplot as plt

tableBinom = PrettyTable()

nBinom = 10
pBinom = 0.3
qBinom = 0.7

fieldNames = ["X"]
for i in range(nBinom + 1):
    fieldNames.append(str(i))

tableBinom.field_names = fieldNames

row = ["P(X)"]
probabilities = []
for m in range(nBinom + 1):
    prob = scipy.special.comb(nBinom, m) * pBinom**m * qBinom**(nBinom - m)
    probabilities.append(prob)
    row.append(f"{prob:.7f}")
tableBinom.add_row(row)
print(tableBinom)

binomSumPx = 0
for m in range(nBinom + 1):
    binomSumPx += scipy.special.comb(nBinom, m) * pBinom**m * qBinom**(nBinom - m)
print(f"sum(P(X)) = {binomSumPx} = 1")

print(f"M(X) = {nBinom*pBinom}")
print(f"D(X) = {nBinom*pBinom*qBinom}")
print(f"Sigma(X) = {sqrt(nBinom*pBinom*qBinom)}")

dictV = {}
for m in range(nBinom + 1):
    dictV[m] = scipy.special.comb(nBinom, m) * pBinom**m * qBinom**(nBinom - m)
maxValues = max(dictV.values())

maxKeys = [key for key, value in dictV.items() if value == maxValues]
print(f'Mo(X) = ', end='')
for el in maxKeys:
    print(el, end=' ')

xValues = list(range(nBinom + 1))
plt.figure(figsize=(10, 5))
plt.plot(xValues, probabilities, 'bo-', linewidth=2, markersize=8)
plt.title('Биномиальное распределение:')
plt.xlabel('X - число забитых мячей')
plt.ylabel('P(X) - вероятность')
plt.grid(True, alpha=0.3)
for i in range(nBinom + 1):
    plt.text(xValues[i], probabilities[i] + 0.01, f'{probabilities[i]:.8f}',
             ha='center', fontsize=9)

plt.tight_layout()
plt.show()