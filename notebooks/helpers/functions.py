import plotly.graph_objs as go


def create_count_plot(data_series, title_text=None, xaxis_title=None):
    """
    This function creates a count plot of the categories in the provided data series.

    Inputs:
    :param data_series (np.series): The data series used to create the count plot.
    :param title_text (str): the title text of the count plot.
    :param xaxis_title (str): the x axis title of the count plot.

    Returns:
    plotly fig.
    """
    # create a plotly go figure
    fig = go.Figure()

    # add trace to figure
    fig.add_trace(go.Bar(x=data_series.index, y=data_series.values))

    # update the layout of the figure
    fig.update_layout(
        plot_bgcolor="white",
        height=450,
        width=475,
        margin={
            "l": 25,
            "r": 25,
            "b": 25,
        },
        title_text=title_text,
        title={
            "x": 0.5,  # position in the middle horizontally
            "xanchor": "center",
            "font": {"size": 14},
        },
        xaxis_title=xaxis_title,
        showlegend=False,
    )
    # update figure x and y axes
    fig.update_xaxes(showline=True, linewidth=1, linecolor="black")
    fig.update_yaxes(showline=True, linewidth=1, linecolor="black")
    fig.show()
