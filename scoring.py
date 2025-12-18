import pandas as pd

df = pd.read_csv("sample_input.csv")

def calculate_score(row):
    score = 0
    score += 30 if row["Role_Fit"] == "Yes" else 0
    score += 20 if row["Funded"] == "Yes" else 0
    score += 40 if row["Scientific_Intent"] == "Yes" else 0
    score += 10 if row["Location_Hub"] == "Yes" else 0
    return score

df["Total_Score"] = df.apply(calculate_score, axis=1)
df = df.sort_values("Total_Score", ascending=False)
df["Rank"] = range(1, len(df) + 1)

df.to_csv("output.csv", index=False)
