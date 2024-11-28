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


plt.title('Гистограмма длины чашелистика (Sepal Length) - Seaborn')
plt.xlabel('Длина чашелистика (cm)')
plt.ylabel('Частота')
plt.grid(True)
#sns.set_style("ваш_стиль")
sns.set_theme(style="ticks")
plt.show()