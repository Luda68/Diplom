import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Загружаем датасет Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, header=None, names=columns)

#matplotlib
plt.figure(figsize=(10, 6))
for species in iris['species'].unique():
    subset = iris[iris['species'] == species]
    plt.hist(subset['sepal_length'], alpha=0.5, bins=10, label=species)


plt.title('Гистограмма длины чашелистика (Sepal Length) - Matplotlib')
plt.xlabel('Длина чашелистика (cm)')
plt.ylabel('Частота')
plt.legend()
plt.grid(True)
plt.show()