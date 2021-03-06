# The plot server must be running
# Go to http://localhost:5006/bokeh to view this plot

import numpy as np
from bokeh.plotting import *

N = 9

x = np.linspace(-2, 2, N)
y = x**2

xpts = np.array([-.09, -.12, .0, .12, .09])
ypts = np.array([-.1, .02, .1, .02, -.1])

output_file("glyphs.html", title="glyphs.py example")

annular_wedge(x, y, 10, 20, 0.6, 4.1, color="#8888ee", tools="pan,zoom,resize", title="annular_wedge")
annulus(x, y, 10, 20, color="#8888ee", tools="pan,zoom,resize", title="annulus")
circle(x, y, 10, color="#8888ee", tools="pan,zoom,resize", title="circle")
line(x, y, color="#8888ee", tools="pan,zoom,resize", title="line")
multi_line([xpts+xx for xx in x], [ypts+yy for yy in y], color="#8888ee", tools="pan,zoom,resize", title="annulus")
oval(x, y, 15, 25, -0.7, color="#8888ee", tools="pan,zoom,resize", title="oval")
patch(x, y, color="#8888ee", tools="pan,zoom,resize", title="square")
patches([xpts+xx for xx in x], [ypts+yy for yy in y], color="#8888ee", tools="pan,zoom,resize", title="annulus")
quad(x, x-0.5, y, y-0.5, color="#8888ee", tools="pan,zoom,resize", title="quad")
ray(x, y, 45, -0.7, color="#8888ee", tools="pan,zoom,resize", title="ray")
rect(x, y, 10, 20, -0.7, color="#8888ee", tools="pan,zoom,resize", title="rect")
segment(x, y, x-0.1, y-0.1, color="#8888ee", tools="pan,zoom,resize", title="segment")
square(x, y, 20, color="#8888ee", tools="pan,zoom,resize", title="square")
wedge(x, y, 15, 0.6, 4.1, color="#8888ee", tools="pan,zoom,resize", title="wedge")

# open a browser
show()

