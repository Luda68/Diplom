import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Загружаем датасет Iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
# список столбцов данных (длина и ширина наружной  и внутренней доли околоцветника)
# и вид ирисов
iris = pd.read_csv(url, header=None, names=columns)


df = sns.load_dataset('iris')


plt.figure(figsize=(10,8), dpi= 80) # dpi - разрешение 80 точек на дюйм
# визуализация с помощью pairplot
sns.pairplot(df, kind="scatter", hue="species", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
# kind="scatter" - построится точечная диаграмма, hue - разделение точек на группы будет
# происходить переменной «species», plot_kws= - настройка параметров парного графика
# с помощью функции pairplot, s=80 - размер маркера, edgecolor - цвет границ "белый",
# linewidth - ширина линии
plt.show()
