import pandas as pd

df = pd.read_csv("../Data-Exploration-Pandas/Data/salaries_by_college_major.csv")

clean_df = df.dropna()

spread_col = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]

# print(spread_col.describe())
# print(spread_col.head())

clean_df.insert(loc=1, column="Spread", value=spread_col)

print(clean_df.head())

low_risk = clean_df.sort_values(by="Spread", ascending=True)
print(low_risk.head())
print(low_risk[["Undergraduate Major", "Spread"]].head())


