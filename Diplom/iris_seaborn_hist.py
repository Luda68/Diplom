import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Загружаем датасет Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, header=None, names=columns)


plt.figure(figsize=(10, 6))
sns.histplot(data=iris, x='sepal_length', hue='species', bins=10, alpha=0.5, kde=False)
# hue - параметром оттенка, bins указывает количество бинов (разбиений) для лучшей
# визуализации, alpha определяет прозрачность графика, а kde=False отключает оценку
# плотности ядра (kernel density estimation, KDE), которая используется для
# сглаживания гистограммы

plt.title('Гистограмма длины чашелистика (Sepal Length) - Seaborn')
plt.xlabel('Длина чашелистика (cm)')
plt.ylabel('Частота')
plt.grid(True) # добавление координатной сетки
#sns.set_style("ваш_стиль")
sns.set_theme(style="ticks") #  добавляет галочки на оси
plt.show()