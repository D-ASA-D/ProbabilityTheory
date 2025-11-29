import numpy as np
import matplotlib.pyplot as plt

sideLength = int(input("Введите длину стороны квадрата:"))
radius = int(input("Введите длину радиуса"))
wallArea = sideLength**2
targetArea = np.pi * radius**2
teorProb = targetArea / wallArea

squareSide = radius * np.sqrt(2)
squareArea = squareSide**2
squareProb = squareArea/wallArea
print(f"Площадь стены: {wallArea}")
print(f"Площадь мешени: {targetArea}")
print(f"Площадь вписанного квадрата: {squareArea}")
print(f"Вероятьность попадания в круг: {teorProb}")
print(f"Вероятьность попадания в квадрат: {squareProb}")

numDarts = int(input(f"Введите колтичество дротиков"))
x = np.random.uniform(-sideLength/2, sideLength/2, numDarts)
y = np.random.uniform(-sideLength/2, sideLength/2, numDarts)
inCircle = (x**2 + y**2)<=radius**2
inSquare = (np.abs(x) <=squareSide/2) & (np.abs(y) <=squareSide/2)
circleHit = np.sum(inCircle)
squareHit = np.sum(inSquare)

simCircleProb = circleHit /numDarts
simSquareProb = squareHit /numDarts

print(f"Смоделированная вероятность попадания в круг: {simCircleProb}")
print(f"Смоделированная вероятность попадания в квадрат: {simSquareProb}")

plt.figure(figsize=(8,8))
outside = ~inCircle
plt.scatter(x[outside], y[outside], color='red', alpha=0.3, s=1, label = 'Вне круга')
inCircleOnly = inCircle & ~inSquare
plt.scatter(x[inCircleOnly], y[inCircleOnly], color = 'blue', alpha=0.5, s=1, label = 'В круге')
plt.scatter(x[inSquare], y[inSquare], color =  'green', alpha=0.7, s=1, label = 'В квадрате')
circle = plt.Circle((0,0), radius, color='blue', fill=False, linewidth=2)
wallSquare = plt.Rectangle((-sideLength/2, -sideLength/2), sideLength, sideLength, color='red', fill=False, linewidth=2)
innerSquare = plt.Rectangle((-squareSide/2, -squareSide/2), squareSide, squareSide, color='green', fill=False, linewidth=2)
plt.gca().add_patch(circle)
plt.gca().add_patch(wallSquare)
plt.gca().add_patch(innerSquare)
plt.axis('equal')
plt.xlim(-sideLength/2, sideLength/2)
plt.ylim(-sideLength/2, sideLength/2)
plt.title(f"Геометрическая вероятность\n"
          f"(Круг) Смоделированная: {simCircleProb} Расчитанная: {teorProb}\n"
          f"(Квадрат) Смоделированная: {simSquareProb} Расчитанная: {squareProb: .4f}")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()