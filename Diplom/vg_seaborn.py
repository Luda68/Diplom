import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "C:/Users/april/Desktop/Urban university/Diplom/vgsales.csv"
vg_data = pd.read_csv(url)

dinamic_by_region = vg_data[
        ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Year_of_Release']
    ].groupby('Year_of_Release').sum()

sns.set_theme(style="darkgrid")  #устанавливается темная сетка фона

# создание линейного графика с помощью функции lineplot
fig = plt.figure(figsize=(12, 6)) # устанавливаем размер фигуры в дюймах (ширина, высота)
lineplot = sns.lineplot(data=dinamic_by_region)
lineplot.set_title('Динамика продаж видеоигр', fontsize=16)
lineplot.set_xlabel('Год выпуска')
lineplot.set_ylabel('Суммарный объём продаж')

plt.show()
