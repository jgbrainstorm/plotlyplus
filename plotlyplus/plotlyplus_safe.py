###
# This module is a simple plug to add plotly express plotting functions to pandas dataframe. different from the plotlypluss, this safe mode add a prefix to the function to avoid messing up the naming space (at a cost of less convinent). 
# Crated By: JHao, 1/26/2023
###
import pandas as pd
import plotly.express as px
pd.DataFrame.px_bar = px.bar
pd.DataFrame.px_area = px.area
pd.DataFrame.px_bar_polar = px.bar_polar
pd.DataFrame.px_box = px.box
pd.DataFrame.px_choropleth = px.choropleth
pd.DataFrame.px_choropleth_mapbox = px.choropleth_mapbox
pd.DataFrame.px_density_contour = px.density_contour
pd.DataFrame.px_density_heatmap = px.density_heatmap
pd.DataFrame.px_density_mapbox = px.density_mapbox
pd.DataFrame.px_ecdf = px.ecdf
pd.DataFrame.px_funnel= px.funnel
pd.DataFrame.px_funnel_area = px.funnel_area
pd.DataFrame.px_get_trendline_results = px.get_trendline_results
pd.DataFrame.px_histogram = px.histogram
pd.DataFrame.px_icicle = px.icicle
pd.DataFrame.px_imshow = px.imshow
pd.DataFrame.px_imshow_utils = px.imshow_utils
pd.DataFrame.px_line = px.line
pd.DataFrame.px_line_3d = px.line_3d
pd.DataFrame.px_line_geo = px.line_geo
pd.DataFrame.px_line_mapbox = px.line_mapbox
pd.DataFrame.px_line_polar = px.line_polar
pd.DataFrame.px_line_ternary = px.line_ternary
pd.DataFrame.px_parallel_categories = px.parallel_categories
pd.DataFrame.px_parallel_coordinates = px.parallel_coordinates
pd.DataFrame.px_pie = px.pie
pd.DataFrame.px_scatter = px.scatter
pd.DataFrame.px_scatter_3d = px.scatter_3d
pd.DataFrame.px_scatter_geo = px.scatter_geo
pd.DataFrame.px_scatter_mapbox = px.scatter_mapbox
pd.DataFrame.px_scatter_matrix = px.scatter_matrix
pd.DataFrame.px_scatter_polar = px.scatter_polar
pd.DataFrame.px_scatter_ternary = px.scatter_ternary
pd.DataFrame.px_set_mapbox_access_token = px.set_mapbox_access_token
pd.DataFrame.px_strip= px.strip
pd.DataFrame.px_timeline = px.timeline
pd.DataFrame.px_treemap = px.treemap
pd.DataFrame.px_trendline_functions = px.trendline_functions
pd.DataFrame.px_violin = px.violin
