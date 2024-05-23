import plotly.express as px
from plotly.subplots import make_subplots
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
    fig.add_trace(go.Bar(x=data_series.index, y=data_series.values, text=data_series.values))

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

def create_histogram_plot(data_series, title_text=None, xaxis_title=None):
    """
    This function creates a histogram plot of the categories in the provided data series.

    Inputs:
    :param data_series (np.series): The data series used to create the histogram plot.
    :param title_text (str): the title text of the histogram plot.
    :param xaxis_title (str): the x axis title of the histogram plot.

    Returns:
    plotly fig.
    """
    # create a plotly go figure
    fig = go.Figure()

    # add trace to figure
    fig.add_trace(go.Histogram(x=data_series.values, text=data_series.values))

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


def create_multivariate_count_plot(data_series, title_text=None, xaxis_title=None, show_text=True):
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
    # create colours dictionary
    colors = {'A':'steelblue',
          'B':'firebrick'}
    
    if show_text:
        # add trace to figure - non defaulters
        fig.add_trace(go.Bar(x=data_series.index, y=data_series[0], name="Non-defaulters", text=data_series[0],  marker_color=colors["A"]))
        # add trace to figure - defaulters
        fig.add_trace(go.Bar(x=data_series.index, y=data_series[1], name="Defaulters",text=data_series[1], marker_color=colors["B"]))
    else:
        # add trace to figure - non defaulters
        fig.add_trace(go.Bar(x=data_series.index, y=data_series[0], name="Non-defaulters", marker_color=colors["A"]))
        # add trace to figure - defaulters
        fig.add_trace(go.Bar(x=data_series.index, y=data_series[1], name="Defaulters", marker_color=colors["B"]))

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


def plot_confusion_matrix(conf_matrix, title=None):
    fig = px.imshow(
        conf_matrix, 
        labels = {
            "x": "Predicted Values",
            "y": "True Value",
            "color": "Productivity"
        },
        x=["No Default", "Default"],
        y=["No Default", "Default"],
        text_auto = True,
        )
    fig.update_xaxes(side="bottom")
    if title:
        fig.update_layout(title=title, title_x=0.5)
    fig.show()