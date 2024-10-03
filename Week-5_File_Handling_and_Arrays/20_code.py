import numpy as np
import matplotlib.pyplot as py_plot

arr = np.random.normal(loc=0.0,scale=1.0,size=10)
py_plot.hist(arr,bins=5,edgecolor="black")
py_plot.title("Histogram")
py_plot.xlabel("Values")
py_plot.ylabel("Frequency")
py_plot.show()
