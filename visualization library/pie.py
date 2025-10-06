import pandas as pd
import matplotlib.pyplot as plt

# Load data
df2 = pd.read_excel("/workspaces/Python-Course/visualization library/Sales Report.xlsx")

# Group by Region and sum Sales
region_sales = df2.groupby("Region")["Sales"].sum()
print(region_sales)

# Plot pie chart
plt.pie(
    region_sales, 
    labels=region_sales.index,      # 🏷️ Displays each region name beside its slice
    autopct="%1.1f%%",              # 🔢 Shows percentage value inside each slice (1 decimal)
    startangle=90,                  # 🔄 Rotates the start of the pie chart to 90° (starts at top)
    explode=(0.1, 0, 0, 0)          # 💥 Pulls out the 1st slice slightly for emphasis
)

plt.title("Sales Distribution by Region")  # 🧾 Adds a title to the chart
plt.savefig("pie.png")                     # 💾 Saves the pie chart as an image file
plt.show()                                 # 👀 Displays the chart on screen
