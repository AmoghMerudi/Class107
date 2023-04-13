import pandas as pd
import csv
import plotly.graph_objects as pe

df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())

figure = pe.Figure(pe.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y = ["Level 1", "Level2", "Level3", "Level4"],
    orientation = "h"
))
figure.show()