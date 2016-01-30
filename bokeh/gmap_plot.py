from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

map_options = GMapOptions(lat=40.331928340222206, lng=-3.765228090336683, map_type="roadmap", zoom=11)

plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="Austin"
)

source = ColumnDataSource(
    data=dict(
        lat=[40.33, 40.34, 40.35],
        lon=[-3.76, -3.77, -3.78],
    )
)

circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)