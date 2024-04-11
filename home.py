import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image


im = Image.open("logo.jpg")
st.set_page_config(
    page_title="Rio Grande Bureau",
    page_icon=im,
    layout="wide",
)

st.subheader('Technical Team', divider='rainbow')

st.title("Snowpack Master")

#st.image("basins.jpg", caption="Location of Basins", width=700, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
 
tab1, tab2 , tab3= st.tabs(["2024 SWE ", "Historical SWE (2007-2023)", "Note"])

with tab1:
    selectbox = st.selectbox(
    'Select a Element',
    ('Snow Water Equivalent (percent)', 
    'Snow Depth (in)')
    )
     
    df = pd.read_excel("data.xlsx")

    if selectbox ==  "Snow Water Equivalent (percent)":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['Rio Chama Basin_Percent of Median'], mode='lines+markers',
                         line=dict(color='deeppink', width=1),
                         marker=dict(color='deeppink', size=8),
                          name='Rio Chama Basin'))
        fig.add_trace(go.Scatter(x = df['Date'], y = df['Upper Rio Grande Basin_Percent of Median'], mode='lines+markers',
                         line=dict(color='blue', width=1),
                         marker=dict(symbol = 'x',color='blue', size=8),
                          name='Upper Rio Grande Basin'))
        fig.add_trace(go.Scatter(x = df['Date'], y = df['SangreDeCristoBasin_PercentofMedian'], mode='lines+markers',
                         line=dict(color='black', width=1),
                         marker=dict(symbol = "triangle-up",color='black', size=8),
                         name='Sangre De Cristo Basin'))
        fig.add_trace(go.Scatter(x = df['Date'], y = df['Jemez River Basin_Percent of Median'], mode='lines+markers',
                         line=dict(color='green', width=1),
                         marker=dict(symbol = 'star',color='green', size=8),
                          name='Jemez River Basin'))
        fig.add_trace(go.Scatter(x = df['Date'], y = df['SanJuanRiverBasin_PercentofMedian'], mode='lines+markers',
                         line=dict(color='gold', width=1),
                         marker=dict(symbol = 'square',color='gold', size=8),
                          name='San Juan River Basin'))
        fig.add_hline( y=100, line_dash='dash',line_color="red",line_width=1)
        fig.update_layout(#title='2024 SWE Percent of Median', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=20, r=20, t=40, b=10),
                   showlegend=True,
                   legend=dict(
                    yanchor="top",
                    y=0.35,
                    xanchor="left",
                    x=0.85),
                    xaxis_range=['2023-11-01','2024-06-01'],
                    yaxis_range=[0,250])
        fig.update_xaxes( showgrid=True)
        #fig.update_layout(xaxis_range=['2023-11-01','2024-06-01'])
        #fig.update_layout(yaxis_range=[0,210])
        #note ='High snowpack percentages are common during the start and end of the snow season when median SWE values are small. https://www.nrcs.usda.gov/conservation-basics/conservation-by-state/montana/montana-snow-survey/frequently-asked-snow-survey-questions-montana'
        #fig.add_annotation(
            #showarrow=False,
            #text=note,
            #font=dict(size=10), 
            #xref='paper',
            #x=0,
            #yref='paper',
            #y=1)
    #fig.update_yaxes(type="log")
    #fig.show()
        st.plotly_chart(fig,use_container_width=True, height = 200)
        st.write('High snowpack percentages are common during the start and end of the snow season when median SWE values are small. \n https://www.nrcs.usda.gov/conservation-basics/conservation-by-state/montana/montana-snow-survey/frequently-asked-snow-survey-questions-montana')
    else:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['Rio Chama Basin_Snow Depth'], mode='lines+markers',
                         line=dict(color='deeppink', width=1),
                         marker=dict(color='deeppink', size=8),
                          name='Rio Chama Basin'))
        fig.add_trace(go.Scatter(x = df['Date'], y = df['UpperRioGrandeBasin_SnowDepth'], mode='lines+markers',
                         line=dict(color='blue', width=1),
                         marker=dict(symbol = 'x',color='blue', size=8),
                          name='Upper Rio Grande Basin'))
        fig.add_trace(go.Scatter(x = df['Date'], y = df['SangreDeCristo Basin_Snow Depth'], mode='lines+markers',
                         line=dict(color='black', width=1),
                         marker=dict(symbol = "triangle-up",color='black', size=8),
                              name='Sangre De Cristo Basin'))
        fig.add_trace(go.Scatter(x = df['Date'], y = df['JemezRiverBasin_SnowDepth'], mode='lines+markers',
                         line=dict(color='green', width=1),
                         marker=dict(symbol = 'star',color='green', size=8),
                         name='Jemez River Basin'))
        fig.add_trace(go.Scatter(x = df['Date'], y = df['San Juan River Basin_Snow Depth'], mode='lines+markers',
                        line=dict(color='gold', width=1),
                        marker=dict(symbol = 'square',color='gold', size=8),
                        name='San Juan River Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=20, r=20, t=40, b=20),
                   showlegend=True,
                   legend=dict(
                    yanchor="top",
                    y=0.3,
                    xanchor="left",
                    x=0.75
                ))
        fig.update_xaxes(minor=dict(ticks="inside", showgrid=True))
        fig.update_layout(xaxis_range=['2023-11-01','2024-06-01'])
        fig.update_layout(yaxis_range=[0,20])
        st.plotly_chart(fig,use_container_width=True, height = 200)



with tab2:  
    add_selectbox1 = st.selectbox(
        'Select a Basin',
        ('Rio Chama Basin', 
        'Upper Rio Grande Basin', 
        'Sangre De Cristo Basin', 
        'Jemez River Basin', 
        'San Juan Basin')
        ,key="x")
    add_selectbox2 = st.selectbox(
        'Select a Element',
        ('Snow Water Equivalent (percent)', 
        'Snow Depth (in)'),
        key="y")

    df = pd.read_excel("data.xlsx") 
    if add_selectbox1 == "Rio Chama Basin" and add_selectbox2 == "Snow Water Equivalent (percent)":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['Rio Chama Basin_Percent of Median'], mode='lines+markers',
                         line=dict(color='deeppink', width=1),
                         marker=dict(color='deeppink', size=3),
                          name='Rio Chama Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=10, r=10, t=50, b=50),
                   showlegend=False,
                   xaxis_range=['2007-12-01','2023-04-05'],
                   yaxis_range=[0,250]
                   )
        fig.update_xaxes( showgrid=True)
    #fig.update_layout(xaxis_range=['2007-12-01','2023-04-05'])
    #fig.update_layout(yaxis_range=[0,1050])
        st.plotly_chart(fig,use_container_width=True, height = 200)
    elif add_selectbox1 == "Upper Rio Grande Basin" and add_selectbox2 == "Snow Water Equivalent (percent)":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['Upper Rio Grande Basin_Percent of Median'], mode='lines+markers',
                         line=dict(color='blue', width=1),
                         marker=dict(symbol = 'x',color='blue', size=3),
                          name='Upper Rio Grande Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=10, r=10, t=50, b=50),
                   showlegend=False,
                   xaxis_range=['2007-12-01','2023-04-05'],
                   yaxis_range=[0,220]
                   )
        fig.update_xaxes(showgrid=True)
    #fig.update_layout(xaxis_range=['2007-12-01','2023-04-05'])
    #fig.update_layout(yaxis_range=[0,1050])
        st.plotly_chart(fig,use_container_width=True, height = 200)
    elif add_selectbox1 == "Sangre De Cristo Basin" and add_selectbox2 == "Snow Water Equivalent (percent)":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['SangreDeCristoBasin_PercentofMedian'], mode='lines+markers',
                         line=dict(color='black', width=1),
                         marker=dict(symbol = "triangle-up",color='black', size=3),
                          name='Sangre Decristo Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=10, r=10, t=50, b=50),
                   showlegend=False,
                   xaxis_range=['2007-12-01','2023-04-05'],
                   yaxis_range=[0,250]
                   )
        fig.update_xaxes(showgrid=True)
    #fig.update_layout(xaxis_range=['2007-12-01','2023-04-05'])
    #fig.update_layout(yaxis_range=[0,1050])
        st.plotly_chart(fig,use_container_width=True, height = 200)
    elif add_selectbox1 == "Jemez River Basin" and add_selectbox2 == "Snow Water Equivalent (percent)":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['Jemez River Basin_Percent of Median'], mode='lines+markers',
                         line=dict(color='green', width=1),
                         marker=dict(symbol = 'star',color='green', size=3),
                          name='Jemez River Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=10, r=10, t=50, b=50),
                   showlegend=False,
                   xaxis_range=['2007-12-01','2023-04-05'],
                   yaxis_range=[0,250]
                   )
        fig.update_xaxes( showgrid=True)
        st.plotly_chart(fig,use_container_width=True, height = 200)
    elif add_selectbox1 == "San Juan River Basin" and add_selectbox2 == "Snow Water Equivalent (percent)":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['SanJuanRiverBasin_PercentofMedian'], mode='lines+markers',
                         line=dict(color='gold', width=1),
                         marker=dict(symbol = 'square',color='gold', size=3),
                          name='San Juan River Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=10, r=10, t=50, b=50),
                   showlegend=False,
                   xaxis_range=['2007-12-01','2023-04-05'],
                   yaxis_range=[0,220]
                   )
        fig.update_xaxes(showgrid=True)
        st.plotly_chart(fig,use_container_width=True, height = 200)
    elif add_selectbox1 == "Rio Chama Basin" and add_selectbox2 == "Snow Depth (in)":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['Rio Chama Basin_Snow Depth'], mode='lines+markers',
                         line=dict(color='deeppink', width=1),
                         marker=dict(color='deeppink', size=3),
                          name='Rio Chama Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=10, r=10, t=50, b=50),
                   showlegend=False,
                   xaxis_range=['2009-1-12','2023-04-05'],
                   yaxis_range=[0,25]
                   )
        fig.update_xaxes( showgrid=True)
    #fig.update_layout(xaxis_range=['2007-12-01','2023-04-05'])
    #fig.update_layout(yaxis_range=[0,25])
        st.plotly_chart(fig,use_container_width=True, height = 200)
    elif add_selectbox1 == "Upper Rio Grande Basin" and add_selectbox2 == "Snow Depth (in)":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['UpperRioGrandeBasin_SnowDepth'], mode='lines+markers',
                         line=dict(color='blue', width=1),
                         marker=dict(symbol = 'x',color='blue', size=3),
                          name='Upper Rio Grande Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=10, r=10, t=50, b=50),
                   showlegend=False,
                   xaxis_range=['2009-1-12','2023-04-05'],
                   yaxis_range=[0,30]
                   )
        fig.update_xaxes(showgrid=True)
    #fig.update_layout(xaxis_range=['2007-12-01','2023-04-05'])
    #fig.update_layout(yaxis_range=[0,25])
        st.plotly_chart(fig,use_container_width=True, height = 200)
    elif add_selectbox1 == "Sangre De Cristo Basin" and add_selectbox2 == "Snow Depth (in)":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['SangreDeCristo Basin_Snow Depth'], mode='lines+markers',
                         line=dict(color='black', width=1),
                         marker=dict(symbol = "triangle-up",color='black', size=3),
                          name='Sangre De Cristo Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=10, r=10, t=50, b=50),
                   showlegend=False,
                   xaxis_range=['2009-1-12','2023-04-05'],
                   yaxis_range=[0,14]
                   )
        fig.update_xaxes( showgrid=True)
    #fig.update_layout(xaxis_range=['2007-12-01','2023-04-05'])
    #fig.update_layout(yaxis_range=[0,25])
        st.plotly_chart(fig,use_container_width=True, height = 200)
    elif add_selectbox1 == "Jemez River Basin" and add_selectbox2 == "Snow Depth (in)":
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['JemezRiverBasin_SnowDepth'], mode='lines+markers',
                         line=dict(color='green', width=1),
                         marker=dict(symbol = 'star',color='green', size=3),
                          name='Jemez River Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=10, r=10, t=50, b=50),
                   showlegend=False,
                   xaxis_range=['2009-1-12','2023-04-05'],
                   yaxis_range=[0,13]
                   )
        fig.update_xaxes( showgrid=True)
        st.plotly_chart(fig,use_container_width=True, height = 200)
    elif add_selectbox1 == "San Juan River Basin" and add_selectbox2 == "Snow Depth (in)": 
        fig = go.Figure()
        fig.add_trace(go.Scatter(x = df['Date'], y = df['San Juan River Basin_Snow Depth'], mode='lines+markers',
                         line=dict(color='gold', width=1),
                         marker=dict(symbol = 'square',color='gold', size=3),
                          name='San Juan River Basin'))
        fig.update_layout(#title='2024 SWE Depth (in)', title_x=0.5,
                   plot_bgcolor='rgb(250, 250,250)',
                   margin=dict(l=10, r=10, t=50, b=50),
                   showlegend=False,
                   xaxis_range=['2009-1-12','2023-04-05'],
                   yaxis_range=[0,38]
                   )
        fig.update_xaxes(showgrid=True)
        st.plotly_chart(fig,use_container_width=True, height = 200)

with tab3:
    col1, col2 = st.columns([1,1.5])
    with col1:
        st.write("Snowpack Mater intends to provide local water management with discrete SWE data. ")
        st.write("Updated subbasins include the Rio Chama Basin, Upper Rio Grande Basin, Sangre De Cristo Basin, Jemez River Basin, and San Juan River Basin.")
        st.write("The delineation of basins is not always consistent with USGS HUC8. The Upper Rio Grande Basin includes the Rio Grande Headwaters, Saguache, and Conejos basins. The Sangre De Cristo Basin includes the San Luis, Alamosa-Trinchem, and Upper Rio Grande basins. The San Juan River Basin includes the Animas, Piedra, and Upper San Juan basins.  ")
    with col2:
        st.image("UplandBasins_SnowpackMaster.jpg", caption="Location of Basins", use_column_width=True, clamp=True, channels="RGB", output_format="auto")
