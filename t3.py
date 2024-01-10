from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import dash_mantine_components as dmc

# Incorporate data
df = pd.read_csv('testData.csv')
# df = px.data.gapminder()

# Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H4("Country's key performance analytics"),
        html.P("Select data on y-axis:"),
        dcc.Dropdown(
            id="y-axis",
            options=["TICV", "wm_vol", "gm_vol"],
            value="TICV",
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(
    Output("graph", "figure"),
    Input("y-axis", "value"),
)
def display_area(y):
    # countries = df.country.drop_duplicates().sample(n=10, random_state=42)
    # dff = df[df.country.isin(countries)]
    fig = px.area(df, x="Age", y=y, color="country")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)