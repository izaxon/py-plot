import pandas as pd
from IPython.display import IFrame
from IPython.core.display import display, HTML

def _get_html(df: pd.DataFrame, index=True):
    csv = df.to_csv(index=index)
    html = f'<html><head><title>VSPlot</title><script src="https://izaxon.github.io/plot/plotly-latest.min.js"></script><script src="https://izaxon.github.io/plot/timeseries-plot.js"></script><link rel="stylesheet" href="https://izaxon.github.io/plot/timeseries-plot.css"></head><body><div id="plot" style="height: 100%;"></div><script>var plotData = `{csv}`; initialize_timeseries_plot({{ zenMode: true, data: plotData }});</script></body></html>';
    return html

def plot(df: pd.DataFrame, index=False, width='100%', height='600px'):
    """ Plots a dataframe using Izaxon Plot (aka VSPlot)
    
    Arguments
        index   include index column of the dataframe   (optional, default = False)
        width   width of HTML window (optional, default = '100%')
        height  height of HTML window (optional, default = '600px')
    """    
    html = _get_html(df, index)
    filename = '_izaxon_plot_iframe.html'
    with open(filename, 'w') as f:
        f.write(html)
    display(IFrame(filename, width, height))

    
