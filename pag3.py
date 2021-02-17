import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
import pandas as pd
import numpy as np


def show_footer():
    st.markdown("***")
    st.markdown("**Like this tool?** Follow me on "
                "[Twitter](https://twitter.com).")

def main():
    st.button("Re-run")

    #set up layout
    st.title("Welcome to the pag3")
    st.markdown("Coming soon ... Sign up [here]() to get notified.")

    #### MAP OPEN-STREET MAP #####
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    st.map(df)

    # #### GRAPH-VISUAL ##### 
    import graphviz as graphviz
    # Create a graphlib graph object
    graph = graphviz.Digraph()
    graph.edge('run', 'intr')
    graph.edge('intr', 'runbl')
    graph.edge('runbl', 'run')
    graph.edge('run', 'kernel')
    graph.edge('kernel', 'zombie')
    graph.edge('kernel', 'sleep')
    graph.edge('kernel', 'runmem')
    graph.edge('sleep', 'swap')
    graph.edge('swap', 'runswap')
    graph.edge('runswap', 'new')
    graph.edge('runswap', 'runmem')
    graph.edge('new', 'runmem')
    graph.edge('sleep', 'runmem')
    st.graphviz_chart(graph)

    # ### SINGLE-TABLE ####
    st.subheader('DATAFRAME')
    df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))
    st.dataframe(df)  # Same as st.write(df)

    ### SINGLE-TABLE - yellowMAX ####
    st.subheader('DATAFRAME WITH MAX UNDERLIANED')
    df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
    st.dataframe(df.style.highlight_max(axis=0))

    ### STATIC TABLE ####
    #Display a static table.
    ''' This differs from st.dataframe in that the table in this case is static: 
    its entire contents are laid out directly on the page.'''
    st.subheader('TABLE')
    df = pd.DataFrame(np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))
    st.table(df)

    ### LINE CHART ####
    st.subheader('LINE CHART')
    chart_data = pd.DataFrame(np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    ### LINE CHART AREA####
    st.subheader('LINE CHART AREA')
    chart_data = pd.DataFrame(np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.area_chart(chart_data)

    #### BAR-CHART #####
    st.subheader('BAR CHART')
    chart_data = pd.DataFrame(np.random.randn(50, 3),
        columns=["a", "b", "c"])

    st.bar_chart(chart_data)

    #### HISTOGRAM-MATPLOTLIB #####
    import matplotlib.pyplot as plt
    st.subheader('HISTOGRAM MATPLOTLIB')

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.pyplot(fig)
  
    #### scatter-ALTAIR #####
    st.subheader('SCATTER ALTAIR')
    import altair as alt
    df = pd.DataFrame(np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.altair_chart(c, use_container_width=True)

    #### PLOTLY #########
    st.subheader('PLOTLY DIAGRAM')
    import plotly.figure_factory as ff
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
    # Plot!
    st.plotly_chart(fig, use_container_width=True)

    #### BOKEH #########
    st.subheader('BOKEH')
    from bokeh.plotting import figure
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    p = figure(title='simple line example',x_axis_label='x',y_axis_label='y')
    p.line(x, y, line_width=2)
    st.bokeh_chart(p, use_container_width=True)

    #### Plotly 2 ################
    import plotly.express as px
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    from numpy import random

    pts = 50
    x1 = np.arange(pts)
    y1 = np.random.rand(pts)
    y2 = np.random.rand(pts)
    y3 = (x1/pts)**2

    fig = make_subplots(rows=1, cols=2)

    fig.add_trace(go.Scatter(x=x1,y=y1,
                        mode='markers',
                        name='markers'),row=1,col=1)
    fig.add_trace(go.Scatter(x=x1,y=y2,
                        mode='markers',
                        name='markers2'),row=1,col=2)
    fig.add_trace(go.Scatter(x=x1,y=y3,
                        mode='lines',
                        name='lines'),row=1,col=2)

    fig.update_layout(height=300, width=800, title_text="Side By Side Subplots")
    st.plotly_chart(fig)


    #### exagonbar-3d ###########################################
    st.subheader('exagon bar-3d')
    import pydeck as pdk
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))

    #### exagonbar-3d ACCIDENT ###########################################

    UK_ACCIDENTS_DATA = ('https://raw.githubusercontent.com/uber-common/'
                        'deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv')

    # Define a layer to display on a map
    layer = pdk.Layer(
        'HexagonLayer',
        UK_ACCIDENTS_DATA,
        get_position=['lng', 'lat'],
        auto_highlight=True,
        elevation_scale=50,
        pickable=True,
        elevation_range=[0, 3000],
        extruded=True,                 
        coverage=1)

    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=-1.415,
        latitude=52.2323,
        zoom=6,
        min_zoom=5,
        max_zoom=15,
        pitch=40.5,
        bearing=-27.36)
    # Render
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

    #### one-image ###########################################
    st.subheader('one-image from URL')
    from PIL import Image
    #image = Image.open('images/cat.jpg')
    image='https://static.streamlit.io/examples/cat.jpg'
    st.image(image,use_column_width=True)

    #### more-images###########################################
    st.subheader('more-images')
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", use_column_width=True)

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", use_column_width=True)


    #### display -code ###########################################
    st.subheader('display code')
    with st.echo():
        st.write('This code will be printed')

    show_footer()
    
if __name__ == "__main__":
    main()