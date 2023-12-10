import numpy as np
import matplotlib.pyplot as plt

x = 12.1
c_min = -10
c_max = 1
c_step = 0.5

c_values = np.arange(c_min, c_max + c_step, c_step)
f_values = []
for c in c_values:
    f_values.append(((abs(2 * x - c) ** 3) ** (1 / 5)) + 0.567)

print("Аргумент | Значение функции")
for c, f in zip(c_values, f_values):
    print("{:.3f} | {:.3f}".format(c, f))

max_f = np.max(f_values)
min_f = np.min(f_values)
mean_f = np.mean(f_values)

n = len(f_values)

for i in range(0, n):
    if i % 2 == 0:
        f_values[i], f_values[n - i - 1] = f_values[n - i - 1], f_values[i]

plt.plot(c_values, f_values, label="f(x)")

#  График ср знач функции f(x)
plt.plot([c_min, c_max], [mean_f, mean_f], label="y = mean(f(x))")

plt.xlabel("c")
plt.ylabel("f(x)")
plt.xlim(c_min, c_max)
plt.ylim(min_f, max_f)

plt.plot(c_values, f_values, marker="o")
plt.plot([c_min, c_max], [mean_f, mean_f], marker="x")

plt.show()
