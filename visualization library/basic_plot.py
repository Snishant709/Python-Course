import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x_val = [1, 3, 5]
y_val = [2, 8, 6]

plt.plot(x_val, y_val)
plt.title("Simple Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

# Save the plot as an image
plt.savefig("plot.png")  

# Show the plot (for local runs) this wont work for github as it is not executes line by line
plt.show()






