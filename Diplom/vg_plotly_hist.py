import pandas as pd
import plotly.express as px

# загружаем данные
url = "C:/Users/april/Desktop/Urban university/Diplom/vgsales.csv"
vg_data = pd.read_csv(url)
dinamic_by_region = vg_data[
        ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Year_of_Release']
    ].groupby('Year_of_Release').sum()

#гистограмма
fig = px.histogram(vg_data, x='Year_of_Release', barmode='overlay', title='Динамика продаж видеоигр - Plotly',
                labels={'Year_of_Release': 'Год выпуска', 'Global_Sales': 'Суммарный объём продаж'})
fig.update_layout(xaxis_title='Год выпуска', yaxis_title='Суммарный объём продаж')
# barmode='overlay' — режим наложения групп гистограммы, при котором они будут
# накладываться друг на друга;  barmode - аргумент, который позволяет указать режим
# диаграммы, например, group, overlay или relative
# labels — метки (подписи) для осей


fig.show()