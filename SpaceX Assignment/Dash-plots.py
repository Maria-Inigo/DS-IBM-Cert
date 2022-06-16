import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc

data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_2.csv', encoding = "ISO-8859-1",)

all_success_data = data[data['Class'] == 1]
all_success_data = all_success_data.groupby(['LaunchSite']).size().reset_index(name='Count')

ratio_CCAFS_data = data[data['LaunchSite'] == 'CCAFS SLC 40']
ratio_CCAFS_data = ratio_CCAFS_data.groupby(['Class']).size().reset_index(name='Count')
ratio_CCAFS_data.replace(0, 'Failure')
ratio_CCAFS_data.replace(1, 'Success')

all_success = px.pie(all_success_data, values='Count', names='LaunchSite', title='Launch sites for successful landings')
ratio_CCAFS = px.pie(ratio_CCAFS_data, values='Count', names='Class', title='Rates of the launch site with most successful landings')
scatterplot = px.scatter(data, x=data['Class'], y=data['PayloadMass'], title='Payload vs. Launch Outcome')

app = dash.Dash(__name__)


# Piechart for the launch success count for all sites
# Piechart for the launch site with highest launch success ratio
# Payload vs. Launch Outcome scatter plot for all sites, with different payload selected in the range slider
app.layout = html.Div(children=[
  html.H1('SpaceX Launch Sites',
    style={
      'textAlign': 'center', 
      'color': '#503D36', 
      'font-size': 40
    }
  ),
  html.Div(
    dcc.Graph(figure=all_success, style={'width': '50vh', 'height': '50vh'}), 
  ),
  html.Div(
    dcc.Graph(figure=ratio_CCAFS, style={'width': '50vh', 'height': '50vh'}), 
  ),
  html.Div(
    dcc.Graph(figure=scatterplot, style={'width': '50vh', 'height': '50vh'}), 
  )
])
                 
if __name__ == '__main__':
  app.run_server()