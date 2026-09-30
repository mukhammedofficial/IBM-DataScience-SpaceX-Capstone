import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

app = Dash(__name__)
spacex_df = pd.read_csv(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
)

min_payload = int(spacex_df["Payload Mass (kg)"].min())
max_payload = int(spacex_df["Payload Mass (kg)"].max())

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40}),
    html.Label("Select a Launch Site"),
    dcc.Dropdown(
        id="site-dropdown",
        options=[{"label": "All Sites", "value": "ALL"}] +
                [{"label": s, "value": s} for s in spacex_df["Launch Site"].unique()],
        value="ALL",
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    html.Br(),
    html.Div(dcc.Graph(id="success-pie-chart")),
    html.Label("Payload range (Kg):"),
    dcc.RangeSlider(
        id="payload-slider",
        min=0, max=10000, step=1000,
        value=[min_payload, max_payload],
        marks={0: "0", 1000: "1000", 2000: "2000", 4000: "4000",
               6000: "6000", 8000: "8000", 10000: "10000"}
    ),
    html.Div(dcc.Graph(id="success-payload-scatter-chart"))
])

@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value")
)
def get_pie_chart(entered_site):
    filtered_df = spacex_df if entered_site == "ALL" else spacex_df[
        spacex_df["Launch Site"] == entered_site
    ]
    if entered_site == "ALL":
        fig = px.pie(
            filtered_df, values="class", names="Launch Site",
            title="Total Success Launches by Site"
        )
    else:
        fig = px.pie(
            filtered_df, names="class",
            title=f"Total Success Launches for site {entered_site}"
        )
    return fig

@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [Input("site-dropdown", "value"),
     Input("payload-slider", "value")]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    filtered_df = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low) &
        (spacex_df["Payload Mass (kg)"] <= high)
    ]
    if entered_site != "ALL":
        filtered_df = filtered_df[filtered_df["Launch Site"] == entered_site]

    fig = px.scatter(
        filtered_df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title="Correlation between Payload and Success for selected sites"
    )
    return fig

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=False)
