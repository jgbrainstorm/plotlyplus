###
# This module is a simple plug to add plotly express plotting functions to pandas dataframe
# Crated By: JHao, 1/26/2023
###
import pandas as pd
import plotly.express as px
pd.DataFrame.bar = px.bar
pd.DataFrame.area = px.area
pd.DataFrame.bar_polar = px.bar_polar
pd.DataFrame.box = px.box
pd.DataFrame.choropleth = px.choropleth
pd.DataFrame.choropleth_mapbox = px.choropleth_mapbox
pd.DataFrame.density_contour = px.density_contour
pd.DataFrame.density_heatmap = px.density_heatmap
pd.DataFrame.density_mapbox = px.density_mapbox
pd.DataFrame.ecdf = px.ecdf
pd.DataFrame.funnel= px.funnel
pd.DataFrame.funnel_area = px.funnel_area
pd.DataFrame.get_trendline_results = px.get_trendline_results
pd.DataFrame.histogram = px.histogram
pd.DataFrame.icicle = px.icicle
pd.DataFrame.imshow = px.imshow
pd.DataFrame.imshow_utils = px.imshow_utils
pd.DataFrame.line = px.line
pd.DataFrame.line_3d = px.line_3d
pd.DataFrame.line_geo = px.line_geo
pd.DataFrame.line_mapbox = px.line_mapbox
pd.DataFrame.line_polar = px.line_polar
pd.DataFrame.line_ternary = px.line_ternary
pd.DataFrame.parallel_categories = px.parallel_categories
pd.DataFrame.parallel_coordinates = px.parallel_coordinates
pd.DataFrame.pie = px.pie
pd.DataFrame.scatter = px.scatter
pd.DataFrame.scatter_3d = px.scatter_3d
pd.DataFrame.scatter_geo = px.scatter_geo
pd.DataFrame.scatter_mapbox = px.scatter_mapbox
pd.DataFrame.scatter_matrix = px.scatter_matrix
pd.DataFrame.scatter_polar = px.scatter_polar
pd.DataFrame.scatter_ternary = px.scatter_ternary
pd.DataFrame.set_mapbox_access_token = px.set_mapbox_access_token
pd.DataFrame.strip= px.strip
pd.DataFrame.timeline = px.timeline
pd.DataFrame.treemap = px.treemap
pd.DataFrame.trendline_functions = px.trendline_functions
pd.DataFrame.violin = px.violin
