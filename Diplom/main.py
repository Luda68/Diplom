import plotly.express as px


geojson = px.data.election_geojson()

# загрузить набор данных
df = px.data.election()


fig = px.choropleth(data_frame=df, geojson=geojson, color="Joly",
                locations="district", featureidkey="properties.district",
                projection="mercator")
#цвет="Joly", местоположение="district", featureidkey принимает путь к полю в объекте
# GeoJSON feature object, с которым должны быть сопоставлены значения, переданные в
# locations, projection принимает вид проекции "mercator"

fig.update_geos(fitbounds="locations", visible=False)
# fitbounds - Если установить значение «locations», то при
# вычислениях fitbounds учитываются только видимые местоположения следа.
# Так как не нужно, чтобы fitbounds были видимыми, устанавливается аргумент visible=False.
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# параметры margin указывают какой отступ задать: l — слева, r — справа, t — сверху, b — снизу.
fig.show()







