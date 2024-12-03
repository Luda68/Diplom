from seaborn._core import data
import matplotlib.pyplot as plt
import numpy as np


# Создадим примерные данные
data = np.random.rand(10, 10)
# Создадим график
plt.imshow(data, cmap='viridis') # указание цветовой карты в библиотеке Matplotlib.
# «Viridis» — одна из встроенных цветовых карт, доступных в Matplotlib. Она представляет
# собой список цветов, где каждый цвет имеет значение от 0 до 100

# Добавим цветовую полосу
plt.colorbar()
plt.show()