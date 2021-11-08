import altair as alt
import altair_viewer
import pandas as pd

Data = pd.read_json('data/cities_data.json')

Links = alt.Chart(Data).mark_circle(size=60).encode(
    x=alt.X('Population'),
    y=alt.Y('Links'),
    color='Type',
    tooltip=['City', 'Links', 'Population', 'Type']
)

altair_viewer.show(Links+Links.transform_regression('Population','Links',groupby=['Type']).mark_line().interactive())
