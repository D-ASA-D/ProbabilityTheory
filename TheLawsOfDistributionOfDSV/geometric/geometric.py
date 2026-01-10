print(f"c) Геометрический закон распределения\n"
      f"Хакер отправляет HTTP запросы на сервер, пока сервер не перестанет работать.\n"
      f"Известно, что вероятность отключения сервера после HTTP запроса равна 0.03.\n"
      f"Случайная величина X - номер запроса, на котором сервер отключился.")

pGeom = 0.03
qGeom = 0.97

from math import sqrt
import matplotlib.pyplot as plt

probsGeom = []
nGeom = 15

for k in range(1, nGeom + 1):
    prob = qGeom**(k-1) * pGeom
    probsGeom.append(prob)

print("\nЗакон распределения (первые 15 значений):")
print("-"*187)
print(f"|  X  |     1     |     2     |     3     |     4     |     5     |     6     |     7     |     8     |     9     |     10    |     11    |     12    |     13    |     14    |     15    |")
print("-"*187)
print("| P(X)|", end="")
for k in range(nGeom):
    print(f" {probsGeom[k]:.7f} |", end="")

print()
print("-"*187)

print("\nФормула расчета:")
print("-"*73)
print(f"|  Z  |   1   |   2   |    3     |    4     |  ...  |     k     |  ...  |")
print("-"*73)
print("| P(Z)|", end="")
print(f"   p   |  q*p  | (q^2)*p  | (q^3)*p  |  ...  | q^(k-1)*p |  ...  |")
print("-"*73)

print(f"p = {pGeom} (вероятность отключения сервера)")
print(f"q = 1-p = {qGeom} (вероятность продолжения работы)")

print(f"M(X) = 1/p = 1/{pGeom} = {1 / pGeom}")

dGeom = qGeom / (pGeom**2)
print(f"D(X) = q/p^2 = {qGeom}/{(pGeom**2):.7f} = {dGeom:.7f}")

sigma_geom = sqrt(dGeom)
print(f"Sigma(X) = sqrt(D(X)) = sqrt({dGeom:.7f}) = {sigma_geom:.27}")


dictV = {}
for m in range(1, nGeom + 1):
    dictV[m] = qGeom**(m-1) * pGeom
maxValues = max(dictV.values())

maxKeys = [key for key, value in dictV.items() if value == maxValues]
print(f'Mo(X) = ', end='')
for el in maxKeys:
    print(el, end=' ')
print()


xValues = list(range(1, nGeom + 1))

plt.figure(figsize=(10, 6))
plt.plot(xValues, probsGeom, 'o-', color='darkorange', linewidth=2, markersize=8)
plt.title(f'Геометрическое распределение:', fontsize=14)
plt.xlabel('X - номер запроса, на котором сервер отключился', fontsize=12)
plt.ylabel('P(X) - вероятность', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(xValues)

for i in range(nGeom):
    plt.text(xValues[i], probsGeom[i] + 0.0005, f'{probsGeom[i]:.4f}',
             ha='center', fontsize=9)

plt.tight_layout()
plt.show()
