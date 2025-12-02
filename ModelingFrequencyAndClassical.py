from random import sample, randint
import plotly.graph_objs as go
import numpy as np
from scipy.special import comb
def random_combination(redBalls, blueBalls, targetRed, targetBlue):
    urna = ['R'] * redBalls + ['B'] * blueBalls
    return sample(urna, targetRed + targetBlue)
while True:
    var = int(input(f"Выбиерите варинат заполнения значений:\n"
          f"1 - ввод с клавиатуры\n"
          f"2 - заполнение случайными числами"))
    if var==1:

        redBalls = int(input("Введите количество красных шаров:"))
        blueBalls = int(input("Введите количество синих шаров:"))
        targetRed = int(input("Введите количество красных вынимаемых шаров:"))
        targetBlue = int(input("Введите количество синих вынимаемых шаров:"))
        break
    elif var==2:
        redBalls = randint(2, 10)
        blueBalls = randint(2, 10)
        targetRed = randint(1, (redBalls+blueBalls)//2)
        targetBlue = randint(1, (redBalls+blueBalls)//2)
        break
    else:
        print("Некорректный ввод повторите попытку")

print(f"Количество красных шаров: {redBalls}")
print(f"Количество синих шаров: {blueBalls}")
print(f"Количество красных вынимаемых шаров: {targetRed}")
print(f"Количество синих вынимаемых шаров: {targetBlue}")
N_values = np.array(range(10, 10001, 50))
P_A_values = []
for N in N_values:
    N_A = 0
    for _ in range(N):
        Comb = random_combination(redBalls, blueBalls, targetRed, targetBlue)
        if Comb.count('R') == targetRed:
            N_A += 1
    P_A_values.append(N_A / N)
pTeor = (comb(redBalls, targetRed) * comb(blueBalls, targetBlue))/comb(redBalls+blueBalls, targetRed+targetBlue)
print(f"Теоретический расчет вероятности: {pTeor}")
print(f"Частотный расчет вероятности: {round(P_A_values[-1], 4)}")
P = [pTeor] * len(N_values)
fig = go.Figure(layout=dict(width=600, height=300))
fig.update_layout(margin=dict(l=0, t=0, b=0))
fig.add_trace(go.Scatter(x=N_values, y=P_A_values, name='Частота'))
fig.add_trace(go.Scatter(x=N_values, y=P,
name='Вероятность', line_dash='dash'))
fig.update_xaxes(title_text='N')
fig.update_yaxes(title_text='P(A)')
fig.show();