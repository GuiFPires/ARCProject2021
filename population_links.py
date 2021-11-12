import altair as alt
import altair_viewer
import altair_transform
import pandas as pd

Data = pd.read_json('data/cities_data.json')

Links = alt.Chart(Data).mark_circle(size=60).encode(
    x=alt.X('Population'),
    y=alt.Y('Links'),
    color='Type',
    tooltip=['City', 'Links', 'Population', 'Type']
)
lines = Links.transform_regression('Population', 'Nodes', groupby=['Type'], params=True).mark_line()
R2_Bike = altair_transform.extract_data(lines)['rSquared'][0]
R2_Drive = altair_transform.extract_data(lines)['rSquared'][1]
R2_Multilayer = altair_transform.extract_data(lines)['rSquared'][2]
R2_Pedestrian = altair_transform.extract_data(lines)['rSquared'][3]
R2_Rail = altair_transform.extract_data(lines)['rSquared'][4]

text = alt.Chart({'values': [{}]}).mark_text(align = "left", baseline = "top").encode(x = alt.value(5), y = alt.value(5),text = alt.value(f"rSquared Bike= {R2_Bike:.4f}"))
text2 = alt.Chart({'values': [{}]}).mark_text(align = "left", baseline = "top").encode(x = alt.value(5), y = alt.value(20),text = alt.value(f"rSquared Drive= {R2_Drive:.4f}"))
text3 = alt.Chart({'values': [{}]}).mark_text(align = "left", baseline = "top").encode(x = alt.value(5), y = alt.value(35),text = alt.value(f"rSquared Pedestrian= {R2_Pedestrian:.4f}"))
text4 = alt.Chart({'values': [{}]}).mark_text(align = "left", baseline = "top").encode(x = alt.value(5), y = alt.value(50),text = alt.value(f"rSquared Rail= {R2_Rail:.4f}"))
text5 = alt.Chart({'values': [{}]}).mark_text(align = "left", baseline = "top").encode(x = alt.value(5), y = alt.value(65),text = alt.value(f"rSquared Multilayered= {R2_Multilayer:.4f}"))

altair_viewer.show(Links+Links.transform_regression('Population','Links',groupby=['Type']).mark_line().interactive() + text + text2 + text3 + text4 + text5)
