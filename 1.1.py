import numpy as np

x = 0.21 * 10**-2

y = (np.sin(x+1)**2 + x * (3 + x**2)**(1/3)) / np.arctan (x/2)

print(f"Ответ равен {y}")