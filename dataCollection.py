import plotly.graph_objects as go
import plotly as py
import math
import sys

from numpy import arange,array,ones
from scipy import stats
#Visualize your data by plotting N vs. d. 
#Linearize your data by plotting ln(N) vs. ln(d).

def squareRoot(l):
    list2 = []
    for i in l:
        list2.append(math.sqrt(int(i)))
    return list2

def naturalLog(l):
    list2 = [math.log(i) for i in l]
    return list2

def errorLn(l1, error):
    list2 = [e / i for e, i in zip(error, l1)]  
    return list2

y=[3276, 2567, 7820, 4009, 1879, 848, 437, 189, 73, 28]
x=[.016, .023, .031, .042, .062, .088, .126, .18, .255, .336]

lnx = naturalLog(x)
lny = naturalLog(y)


yerror = squareRoot(y)
xerror = [.0005] * 10

lnyError = errorLn(y, yerror)
lnxError =  errorLn(x, xerror)

slope, intercept, r_value, p_value, std_err = stats.linregress(lnx, lny)
line = slope*array(lnx)+intercept

print(slope)
print(intercept)

layout = go.Layout(
    title = "Distance vs Corrected Radiation",
    xaxis = dict(
        title = "Distance (m)",
    ),
    yaxis = dict(
        title = "Corrected Radiation (counts/int)",
    ),
       font=dict(
        family="Courier New, monospace",
        size=18,
    )
)

layout2 = go.Layout(
    title = "Ln(Distance) vs Ln(Corrected Radiation)",
    xaxis = dict(
        title = "Ln(Distance)",
    ),
    yaxis = dict(
        title = "Ln(Corrected Radiation)",
    ),
       font=dict(
        family="Courier New, monospace",
        size=18,
    )
)

NvD = go.Scatter(
        x=x,
        y=y,
        mode='markers',
        error_y=dict(
            type='data', # value of error bar given in data coordinates
            array=yerror,
            visible=True),

        error_x=dict(
            type='data', # value of error bar given in data coordinates
            array=xerror,
            visible=True)
        )
   
Ln = go.Scatter(
        x=lnx,
        y=lny,
        mode='markers',
        name='data points',
        error_y=dict(
            type='data', # value of error bar given in data coordinates
            array=lnyError,
            visible=True),

        error_x=dict(
            type='data', # value of error bar given in data coordinates
            array=lnxError,
            visible=True)
        )

line = go.Scatter(
                  x=lnx,
                  y=line,
                  mode='lines',
                  marker=go.Marker(color='rgb(31, 119, 180)'),
                  name='Linear Regression'
                  )

data1 = [NvD]
fig1 = go.Figure(data=data1,layout=layout)

data2 = [Ln, line]
fig2 = go.Figure(data=data2,layout=layout2)

print(lnx)
py.offline.plot(fig2, filename='dataCollection')