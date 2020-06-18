import pysd
import dash
import dash_core_components as dcc
import dash_html_components as html

model = pysd.read_vensim("AdditionalSources/Model16Final.mdl")

def set_baseCase():
    params = {
        "policy_switch_1_water_demand_reduction" : 0,
        "external_switch_1_dry_climate" : 0,
        "external_switch_2_wet_climate" : 0,
        "external_switch_3_low_international_food_prices" : 0,
        "external_switch_4_high_international_food_prices" : 0,
    }
    output = model.run(params=params)
    return output

#Create Dashboard
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

sdApp = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = sdApp.server

sdApp.layout = html.Div(children=[
    html.Div(className="row", children=[
        html.Div(className= "twelve columns", children=[
            html.H1("Efficiency irrigation Egypt: Interactive SD modelling dashboard"),
            html.P("This project uses PySD and Dash to simulate a System Dynamics model build in Vensim and visualize the results on an interactive dashboard. The SD model is built in the context of a bachelor final project on effects of irrigation efficiency improvements in Egypt. This research is performed in the context of the Technology, Policy and Management bachelor thesis program of the Technical University Delft. The goal of this research is to inform local policymakers in Egypt best about possible effects of improved irrigation efficiency. In consideration of this goal, an interactive dashboard using Python is built to enable policymakers to simulate the constructed model in this research without any additional knowledge requirements about simulations and visualizations. Furthermore, the dashboard enables policymakers to test a wide range of variations in model input combinations, since the model is simulated in the background (PySD) in real time."),
            html.P([html.Br(), "For all dependencies and additional information see ", html.A("Github", href="https://github.com/floristevito/DashSD", style={"color" : "black"})]),
        ],
                style={"background-color" : "#66a3ff"}
                ),
    ]),
    html.Div(className="row", children=[
        html.Div(className= "four columns", children=[
            html.H2("Input parameters"),
            html.P("Input parameters that can be changed to experiment with modelling results. The model will be simulated in real time and might take a small amount of time to fully load. Note that when an efficiency stimulating policy is enabled, the sliders should also be given an appropriate value. Otherwise, the model will run but inaccurate results will be produced. Press the run simulation button when the parameters are set to preferences."),
            html.Button("Run simulation", id="Run", style={"float":"right"}),
            html.H3("Policy and climate scenarios"),
            html.Label("Efficient irrigation policy"),
            dcc.Dropdown(
                id="dropdownPolicy",
                options=[{"label" : "No policy", "value" : "None"},
                         {"label" : "Efficiency stimulating policy", "value" : "Efficiency"}
                ],
                value="None" 
            ),
            html.Label("Climate scenario"),
            dcc.Dropdown(
                id="dropdownClimate",
                options=[{"label" : "Base case", "value" : "None"},
                         {"label" : "Dry upper Nile climate conditions", "value" : "Dry"},
                         {"label" : "Wet upper Nile climate conditions", "value" : "Wet"}
                ],
                value="None" 
            ),
            html.Label("International food prices scenario"),
            dcc.Dropdown(
                id="dropdownFood",
                options=[{"label" : "Base case", "value" : "None"},
                         {"label" : "High international food prices", "value" : "High"},
                         {"label" : "Low international food prices", "value" : "Low"}
                ],
                value="None" 
            ),
            html.H3("Sliders for policy scenario"),
            html.P("Important: the sum of both the new and decreased land should always equal 100% for accurate results"),
            html.Label("Percentage of new irrigated land Surface Irrigated"),
            dcc.Slider(
                id="sliderNewSurface",
                min = 0,
                max = 100,
                step = 10,
                marks = {
                    0: {"label" : "0%"},
                    10: {"label" : "10%"},
                    20: {"label" : "20%"},
                    30: {"label" : "30%"},
                    40: {"label" : "40%"},
                    50: {"label" : "50%"},
                    60: {"label" : "60%"},
                    70: {"label" : "70%"},
                    80: {"label" : "80%"},
                    90: {"label" : "90%"},
                    100: {"label" : "100%"},
                },
                value = 0,
            ),
            html.Label("Percentage of new irrigated land Sprinkler Irrigated"),
            dcc.Slider(
                id="sliderNewSprinkler",
                min = 0,
                max = 100,
                step = 10,
                marks = {
                    0: {"label" : "0%"},
                    10: {"label" : "10%"},
                    20: {"label" : "20%"},
                    30: {"label" : "30%"},
                    40: {"label" : "40%"},
                    50: {"label" : "50%"},
                    60: {"label" : "60%"},
                    70: {"label" : "70%"},
                    80: {"label" : "80%"},
                    90: {"label" : "90%"},
                    100: {"label" : "100%"},
                },
                value = 0,
            ),
            html.Label("Percentage of new irrigated land Localized Irrigated"),
            dcc.Slider(
                id="sliderNewLocalized",
                 min = 0,
                max = 100,
                step = 10,
                marks = {
                    0: {"label" : "0%"},
                    10: {"label" : "10%"},
                    20: {"label" : "20%"},
                    30: {"label" : "30%"},
                    40: {"label" : "40%"},
                    50: {"label" : "50%"},
                    60: {"label" : "60%"},
                    70: {"label" : "70%"},
                    80: {"label" : "80%"},
                    90: {"label" : "90%"},
                    100: {"label" : "100%"},
                },
                value = 0,
            ),
            html.Label("Percentage of decreased irrigated land Surface Irrigated"),
            dcc.Slider(
                id="sliderDecrSurface",
                 min = 0,
                max = 100,
                step = 10,
                marks = {
                    0: {"label" : "0%"},
                    10: {"label" : "10%"},
                    20: {"label" : "20%"},
                    30: {"label" : "30%"},
                    40: {"label" : "40%"},
                    50: {"label" : "50%"},
                    60: {"label" : "60%"},
                    70: {"label" : "70%"},
                    80: {"label" : "80%"},
                    90: {"label" : "90%"},
                    100: {"label" : "100%"},
                },
                value = 0,
            ),
            html.Label("Percentage of decreased irrigated land Sprinkler Irrigated" ),
            dcc.Slider(
                id="sliderDecrSprinkler",
                min = 0,
                max = 100,
                step = 10,
                marks = {
                    0: {"label" : "0%"},
                    10: {"label" : "10%"},
                    20: {"label" : "20%"},
                    30: {"label" : "30%"},
                    40: {"label" : "40%"},
                    50: {"label" : "50%"},
                    60: {"label" : "60%"},
                    70: {"label" : "70%"},
                    80: {"label" : "80%"},
                    90: {"label" : "90%"},
                    100: {"label" : "100%"},
                },
                value = 0,
            ),
            html.Label("Percentage of decreased irrigated land Localized Irrigated"),
            dcc.Slider(
                id="sliderDecrLocalized",
                min = 0,
                max = 100,
                step = 10,
                marks = {
                    0: {"label" : "0%"},
                    10: {"label" : "10%"},
                    20: {"label" : "20%"},
                    30: {"label" : "30%"},
                    40: {"label" : "40%"},
                    50: {"label" : "50%"},
                    60: {"label" : "60%"},
                    70: {"label" : "70%"},
                    80: {"label" : "80%"},
                    90: {"label" : "90%"},
                    100: {"label" : "100%"},
                },
                value = 0,
            ),
            ],
            style={"background-color" : "#b3d1ff"}),
        html.Div(className= "eight columns", children=[
            dcc.Graph(
                id="Agricultural water shortage Egypt",
                style={"float":"left", "width": "49.5%"}
            ),
            dcc.Graph(
                id="Agricultural water shortage Egypt with import",
                style={"float":"left", "width": "49.5%"}
            ),
            dcc.Graph(
                id="Percentage recovered",
                style={"float":"left", "width": "49.5%"}
            ),
            dcc.Graph(
                id="Effective irrigated land",
                style={"float":"left", "width": "49.5%"}
            ),
            dcc.Graph(
                id="Agricultural production",
                style={"float":"left", "width": "49.5%"}
            ),
            dcc.Graph(
                id="Water demand per irrigated area",
                style={"float":"left", "width": "49.5%"}
            ),
            dcc.Graph(
                id="Water use for irrigation",
                style={"float":"left", "width": "99%"}
            ),
            dcc.Loading(id="loading", children=html.Div(id="loading-output"), style={"height": "80%"}),
            ],
            style={"background-color" : "#e6f0ff"}) 
        ])
])

#Callbacks
@sdApp.callback(
    [dash.dependencies.Output('loading-output', 'children'),
    dash.dependencies.Output('Agricultural water shortage Egypt', 'figure'),
    dash.dependencies.Output('Agricultural water shortage Egypt with import', 'figure'),
    dash.dependencies.Output('Percentage recovered', 'figure'),
    dash.dependencies.Output('Effective irrigated land', 'figure'),
    dash.dependencies.Output('Agricultural production', 'figure'),
    dash.dependencies.Output('Water demand per irrigated area', 'figure'),
    dash.dependencies.Output('Water use for irrigation', 'figure')], 
    [dash.dependencies.Input("Run", "n_clicks"),
    dash.dependencies.Input("loading", "value")],
    [dash.dependencies.State('dropdownPolicy', 'value'),
    dash.dependencies.State('dropdownClimate', 'value'),
    dash.dependencies.State('dropdownFood', 'value'),
    dash.dependencies.State('sliderNewSurface', 'value'),
    dash.dependencies.State('sliderNewSprinkler', 'value'),
    dash.dependencies.State('sliderNewLocalized', 'value'),
    dash.dependencies.State('sliderDecrSurface', 'value'),
    dash.dependencies.State('sliderDecrSprinkler', 'value'),
    dash.dependencies.State('sliderDecrLocalized', 'value')
    ])
     

def update_water_shortage(n_clicks, value, valuePolicy, valueClimate, valueFood, valueNewSurface, valueNewSprinkler, valueNewLocalized, valueDecrSurface, valueDecrSprinkler, valueDecrLocalized):
    switchP1= 1 if  valuePolicy == "Efficiency" else 0
    switchE1 = 1 if valueClimate == "Dry" else 0 
    switchE2 = 1 if valueClimate == "Wet" else 0 
    switchE3 = 1 if valueFood == "Low" else 0 
    switchE4 = 1 if valueFood == "High" else 0 
    params = {
        "policy_switch_1_water_demand_reduction" : switchP1,
        "external_switch_1_dry_climate" : switchE1, 
        "external_switch_2_wet_climate" : switchE2,
        "external_switch_3_low_international_food_prices" : switchE3, 
        "external_switch_4_high_international_food_prices" : switchE4,
        "percentage_of_new_land_surface_irrigated" : valueNewSurface, 
        "percentage_of_decreased_land_surface_irrigated" : valueDecrSurface,
        "percentage_of_new_land_sprinkler_irrigated" : valueNewSprinkler, 
        "percentage_of_decreased_land_sprinkler_irrigated" : valueDecrSprinkler,
        "percentage_of_new_land_localized_irrigated" : valueNewLocalized, 
        "percentage_of_decreased_land_localized_irrigated" : valueDecrLocalized
    }
    base = set_baseCase()
    output =  model.run(params=params)
    base["Percentage recovered"] = base["Percentage recovered"].round(2)
    output["Percentage recovered"] = output["Percentage recovered"].round(2)
    figureWaterShortage = {
            "data" : [
                {"x": base["Agricultural water shortage"].index.tolist(), "y": base["Agricultural water shortage"].values.tolist(),
                "type" : "graph", "name" : "base case"},
                {"x": output["Agricultural water shortage"].index.tolist(), "y": output["Agricultural water shortage"].values.tolist(),
                "type" : "graph", "name" : "selected scenario"}],
            "layout" : {
                "title" : "Agricultural water shortage Egypt",
                "xaxis" : {"title" : "year"},
                "yaxis" : {"title" : "cubic meters water per year"}
                }
            }
    figureWaterShortageImport = {
            "data" : [
                {"x": base["Agricultural water shortage with import"].index.tolist(), "y": base["Agricultural water shortage with import"].values.tolist(),
                "type" : "graph", "name" : "base case"},
                {"x": output["Agricultural water shortage with import"].index.tolist(), "y": output["Agricultural water shortage with import"].values.tolist(),
                "type" : "graph", "name" : "selected scenario"}],
            "layout" : {
                "title" : "Agricultural water shortage Egypt with import",
                "xaxis" : {"title" : "year"},
                "yaxis" : {"title" : "cubic meters water per year"}
                }
            }
    figurePercentageRecovered = {
            "data" : [
                {"x": base["Percentage recovered"].index.tolist(), "y": base["Percentage recovered"].values.tolist(),
                "type" : "graph", "name" : "base case"},
                {"x": output["Percentage recovered"].index.tolist(), "y": output["Percentage recovered"].values.tolist(),
                "type" : "graph", "name" : "selected scenario"}],
            "layout" : {
                "title" : "Percentage of irrigated water volume recovered",
                "xaxis" : {"title" : "year"},
                "yaxis" : {"title" : "%"}
                }
            }
    figureEffectiveLand = {
            "data" : [
                 {"x": base["Effective irrigated land"].index.tolist(), "y": base["Effective irrigated land"].values.tolist(),
                "type" : "graph", "name" : "base case"},
                {"x": output["Effective irrigated land"].index.tolist(), "y": output["Effective irrigated land"].values.tolist(),
                "type" : "graph", "name" : "selected scenario"}],
            "layout" : {
                "title" : "Effective irrigated land",
                "xaxis" : {"title" : "year"},
                "yaxis" : {"title" : "Square kilometers"}
                }
            }
    figureAgriculturalProduction = {
            "data" : [
                {"x": base["Agricultural production"].index.tolist(), "y": base["Agricultural production"].values.tolist(),
                "type" : "graph", "name" : "base case"},
                {"x": output["Agricultural production"].index.tolist(), "y": output["Agricultural production"].values.tolist(),
                "type" : "graph", "name" : "selected scenario"}],
            "layout" : {
                "title" : "Agricultural production",
                "xaxis" : {"title" : "year"},
                "yaxis" : {"title" : "Kilograms per year"}
                }
            }
    figureWaterDemand = {
            "data" : [
                {"x": base["Water demand per irrigated area"].index.tolist(), "y": base["Water demand per irrigated area"].values.tolist(),
                "type" : "graph", "name" : "base case"},
                {"x": output["Water demand per irrigated area"].index.tolist(), "y": output["Water demand per irrigated area"].values.tolist(),
                "type" : "graph", "name" : "selected scenario"}],
            "layout" : {
                "title" : "Water demand per irrigated area",
                "xaxis" : {"title" : "year"},
                "yaxis" : {"title" : "Cubic meter/square kilometer/year"}
                }
            }
    figureWaterUse = {
            "data" : [
                {"x": base["Water use for irrigation"].index.tolist(), "y": base["Water use for irrigation"].values.tolist(),
                "type" : "graph", "name" : "base case"},
                {"x": output["Water use for irrigation"].index.tolist(), "y": output["Water use for irrigation"].values.tolist(),
                "type" : "graph", "name" : "selected scenario"}],
            "layout" : {
                "title" : "Water use for irrigation",
                "xaxis" : {"title" : "year"},
                "yaxis" : {"title" : "Cubic meter per year"}
                }
            }
    
    return value, figureWaterShortage, figureWaterShortageImport, figurePercentageRecovered, figureEffectiveLand, figureAgriculturalProduction, figureWaterDemand, figureWaterUse

#Load Dashboard
if __name__ == '__main__':
    sdApp.run_server(debug=True)