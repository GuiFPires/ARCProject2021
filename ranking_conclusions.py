import altair as alt
import altair_viewer
import altair_transform
import pandas as pd

Data = pd.read_json('data/overlap_data.json')

Nodes = alt.Chart(Data).mark_circle(size=60).encode(
    x=alt.X('Pedestrian-Drive Overlap Census'),
    y=alt.Y('Congestion Level'),
    color='Type',
    tooltip=['City', 'Pedestrian-Drive Overlap Census', 'Congestion Level', 'Type']
)
line = Nodes.transform_regression('Pedestrian-Drive Overlap Census','Congestion Level', params=True).mark_line()
R2 = altair_transform.extract_data(line)['rSquared'][0]
text = alt.Chart({'values': [{}]}).mark_text(align = "left", baseline = "top").encode(x = alt.value(5), y = alt.value(5),text = alt.value(f"rSquared = {R2:.4f}"),)
altair_viewer.show(Nodes+Nodes.transform_regression('Pedestrian-Drive Overlap Census','Congestion Level').mark_line().interactive() + text)