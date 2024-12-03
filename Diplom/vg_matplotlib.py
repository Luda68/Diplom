import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
import seaborn as sns
import mplcyberpunk


# Загружаем данные из csv файла
url = "C:/Users/april/Desktop/Urban university/Diplom/vgsales.csv"
vg_data = pd.read_csv(url)

# график динамики продаж видеоигр в зависимости от региона. По оси ординат отложено
# число проданных дисков с видеоиграми (в миллионах) в различных регионах
# (NA — Северная Америка, EU — Европа, JP — Япония, Other — другие регионы,
# Global — во всём мире), по оси абсцисс — год выпуска игры.
dinamic_by_region = vg_data[
        ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Year_of_Release']
    ].groupby('Year_of_Release').sum()

# стиль графика
style.use("cyberpunk")

# линейный график matplotlib
fig = plt.figure(figsize=(12, 6)) # создаём объект Figure с заданным размером изображения в дюймах
lineplot = sns.lineplot(data=dinamic_by_region)
lineplot.set_title('Динамика продаж видеоигр', fontsize=16) # размер шрифта элемента
# установлен в пикселях, это значение используется по умолчанию в большинстве браузеров
lineplot.set_xlabel('Год выпуска')
lineplot.set_ylabel('Суммарный объём продаж')

plt.show()
