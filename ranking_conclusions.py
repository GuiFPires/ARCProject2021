import altair as alt
import altair_viewer
import pandas as pd

Data = pd.read_json('data/overlap_data.json')

Nodes = alt.Chart(Data).mark_circle(size=60).encode(
    x=alt.X('Pedestrian-Drive Overlap Census'),
    y=alt.Y('Congestion Level'),
    color='Type',
    tooltip=['City', 'Pedestrian-Drive Overlap Census', 'Congestion Level', 'Type']
)

altair_viewer.show(Nodes+Nodes.transform_regression('Pedestrian-Drive Overlap Census','Congestion Level').mark_line().interactive())
