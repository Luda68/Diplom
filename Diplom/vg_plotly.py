import pandas as pd
import plotly.express as px


url = "C:/Users/april/Desktop/Urban university/Diplom/vgsales.csv"
vg_data = pd.read_csv(url)
dinamic_by_region = vg_data[
        ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Year_of_Release']
    ].groupby('Year_of_Release').sum()

# линейный график
fig = px.line(vg_data, x='Year_of_Release', y='Global_Sales', title='Динамика продаж видеоигр - Plotly',
                labels={'Year_of_Release': 'Год выпуска', 'Global_Sales': 'Суммарный объём продаж'}).update_layout(font_size=15)
# update_layout(font_size=15) установление размера шрифта для какого-либо элемента макета
# графика, например, заголовка или меток осей.

# настраиваем заголовки осей
fig.update_layout(xaxis_title='Год выпуска', yaxis_title='Суммарный объём продаж')


fig.show()