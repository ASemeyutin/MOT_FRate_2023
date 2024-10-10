# =========================================================================================================== #
#
from pathlib import Path  
import pandas as pd
import geopandas as gpd
import folium
import matplotlib
import mapclassify
from shiny import App, render, ui
#
# =========================================================================================================== #
#
fname_MOT_2023 = Path(__file__).parent / "FR23.csv"
fname_geo_bndr = Path(__file__).parent / "postcode-boundaries.geojson"
FR23 = pd.read_csv(fname_MOT_2023)
geodf = gpd.read_file(fname_geo_bndr)
#
FR23 = FR23.rename({
    'postcode_area': 'Postcode Area',
    'FRall' : 'All vehicles (ignoring age)',
    'FR34' : '3 to 4 years old vehicles',
    'FR45' : '4 to 5 years old vehicles',
    'FR56' : '5 to 6 years old vehicles',
    'FR67' : '6 to 7 years old vehicles',
    'FR78' : '7 to 8 years old vehicles',
    'FR89' : '8 to 9 years old vehicles',
    'FR910' : '9 to 10 years old vehicles',
    'FRm10' : '10 years and older vehicles',
}, axis = 1)
#
geodf = geodf.rename({'Name': 'Postcode Area', 'geometry': 'geometry'}, axis = 1)
FR23geo = geodf.merge(FR23, on = 'Postcode Area').set_index('Postcode Area')
#
# =========================================================================================================== #
#
app_ui = ui.page_fluid(
    ui.h2(
        "Mapping UK 2023 MOT Failure Rates by the Posctode Area", 
        style = "color: darkgreen; font-size: 24px; text-align: left; font-weight: bold;" 
    ),
    ui.input_select("column", "Select MOT Failure Rate for:", choices = FR23geo.columns.tolist()[1:10]),
    ui.div(
        ui.output_ui("myplot"), 
        style = (
            "width: 1200px; height: 600px; "
            "border: 2px solid green; "
            "border-radius: 8px; "
            "padding: 2.5px; "
            "background-color: #f9f9f9; "
            "box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); "
            "overflow: auto;"
        )
    )
)
# 
def server(input, output, session):
    @output
    @render.ui
    def myplot():
        MOTMAP23 = FR23geo.explore(
                column = input.column(),  
                scheme = "naturalbreaks",
                legend = True,  
                k = 15,  
                tooltip = False,  
                popup = ["Postcode Area", input.column()],  
                legend_kwds = dict(colorbar = True),  
                style_kwds = dict(color = "black", weight = 1, opacity = 0.4, fillOpacity = .7),
                name = "Polygon", 
                cmap = 'Greens',
                location = [54.5, -2.5], 
                zoom_start = 5.25
            )
        return MOTMAP23
# 
app = App(app_ui, server)
#
# =========================================================================================================== #