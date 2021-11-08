import altair as alt
import altair_viewer
import pandas as pd

Data = pd.read_json('data/cities_data.json')

Nodes = alt.Chart(Data).mark_circle(size=60).encode(
    x=alt.X('Population'),
    y=alt.Y('Nodes'),
    color='Type',
    tooltip=['City', 'Nodes', 'Population', 'Type']
)

altair_viewer.show(Nodes+Nodes.transform_regression('Population', 'Nodes', groupby=['Type']).mark_line().interactive())
