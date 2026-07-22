import pandas as pd
import random

df = pd.read_excel("TASKS.xlsx")

# Clean column names
df.columns = df.columns.str.strip()

# Clean the NAME column
df["NAME"] = df["NAME"].str.strip().str.upper()

name = "ROHIT".strip().upper()

row = df[df["NAME"] == name]

print(row)
print("Matching rows:", len(row))

tasks = row.iloc[0, 1:].dropna().tolist()

print("Tasks:", tasks)

task = random.choice(tasks)

print("Random Task:", task)