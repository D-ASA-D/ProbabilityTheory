import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_continuous
from scipy import integrate

class CustomDistribution(rv_continuous):
    def __init__(self, a, b):
        super().__init__(a=a, b=b, name='custom_quad_dist')

    def _pdf(self, x):
        """Плотность распределения"""
        result = np.zeros_like(x)
        result[(x >= self.a) & (x <= self.b)] = 3 * (x - 1)**2
        return result

    def _cdf(self, x):
        """Функция распределения"""
        result = np.zeros_like(x)
        result[x < self.a] = 0
        result[(x >= self.a) & (x <= self.b)] = (x - 1)**3
        result[x > self.b] = 1
        return result

    def _ppf(self, q):
        """Обратная функция распределения (квантильная функция)"""
        return 1 + q ** (1/3)


a, b = 1.0, 2.0
custom_dist = CustomDistribution(a, b)

sample = custom_dist.rvs(size=10000)

print(f"Размер выборки: {len(sample)}")
print(f"Первые 10 значений: {sample[:10]}")

print("\nПроверка нормировки плотности")
integral, error = integrate.quad(custom_dist.pdf, a, b)
print(f"∫ f(x) dx на [{a}, {b}] = {integral:.6f} (ошибка: {error:.2e})")

print("\nПроверка в граничных точках:")
print(f"F({a}) = {custom_dist.cdf(a):.6f}")
print(f"F({b}) = {custom_dist.cdf(b):.6f}")

x1, x2 = 1.2, 1.7
prob = custom_dist.cdf(x2) - custom_dist.cdf(x1)
print("\nВЕРОЯТНОСТЬ НА ИНТЕРВАЛЕ")
print(f"P({x1} ≤ X ≤ {x2}) = {prob:.6f}")

print("\nЧИСЛОВЫЕ ХАРАКТЕРИСТИКИ")
print(f"Математическое ожидание: {custom_dist.mean():.4f}")
print(f"Дисперсия: {custom_dist.var():.4f}")
print(f"Среднее квадратическое отклонение: {custom_dist.std():.4f}")

mean, var, skew, kurt = custom_dist.stats(moments='mvsk')
print(f"\nАсимметрия: {skew:.4f}")
print(f"Эксцесс: {kurt:.4f}")

q = 0.9
print(f"\nКвантиль уровня {q}: {custom_dist.ppf(q):.4f}")
print(f"90%-ная точка: {custom_dist.ppf(1-q):.4f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))
x_plot = np.linspace(a - 0.2, b + 0.2, 1000)

ax1.hist(sample, bins=50, density=True, cumulative=True,
         alpha=0.7, label='Эмпирическая CDF')
ax1.plot(x_plot, custom_dist.cdf(x_plot),
         'r-', linewidth=2, label='Теоретическая CDF')
ax1.set_xlabel('x')
ax1.set_ylabel('F(x)')
ax1.set_title('Функция распределения')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.hist(sample, bins=50, density=True,
         alpha=0.7, label='Выборка')
ax2.plot(x_plot, custom_dist.pdf(x_plot),
         'r-', linewidth=2, label='Теоретическая PDF')
ax2.set_xlabel('x')
ax2.set_ylabel('Плотность вероятности')
ax2.set_title('Гистограмма и теоретическая плотность')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.show()


