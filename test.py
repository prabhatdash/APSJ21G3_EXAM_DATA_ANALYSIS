import pandas as pd

df=pd.read_csv('StudentsPerformance.csv',engine="python")
print(df["math_score"].max(), "  -Highest math score")
print(df["reading score"].max(), "  -Highest reading score")
print(df["writing score"].max(), "  -Highest writing score")
