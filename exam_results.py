import pandas as pd

data = pd.read_csv("results.csv")

print("Exam Results:")
print(data)

print("\nAverage Marks:")
print(data["Marks"].mean())

print("\nHighest Marks:")
print(data["Marks"].max())