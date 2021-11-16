import pandas as pd

df = pd.read_csv("../Data-Exploration-Pandas/Data/salaries_by_college_major.csv")

clean_df = df.dropna()

print("Enter the following command to find the highest paying college major.")
print("Enter 1 for College major with Highest/Lowest Starting Median Salary")
print("Enter 2 for College major with Highest/Lowest Mid Carrier Median Salary")
print("Enter 3 for College major with Highest/Lowest Mid-Career 10th Percentile Salary")
print("Enter 4 for College major with Highest/Lowest Mid-Career 90th Percentile Salary")

# choice = int(input("Choice: "))

def paying_major(choice = "Starting Median Salary"):
    if choice == 1:
        ch = "Starting Median Salary"
    elif choice == 2:
        ch = "Mid-Career Median Salary"
    elif choice == 3:
        ch = "Mid-Career 10th Percentile Salary"
    else:
        ch = "Mid-Career 90th Percentile Salary"

    def highest_paying_college_major(ch):
        id_max = clean_df[ch].idxmax()
        # print(f"ch = {ch}\nid_max = {id_max}")
        return clean_df["Undergraduate Major"].loc[id_max]

    def lowest_paying_college_major(ch):
        id_min = clean_df[ch].idxmin()
        # print(f"ch = {ch}\nid_min = {id_min}")
        return clean_df["Undergraduate Major"].loc[id_min]

    print(f"Highest paying major {highest_paying_college_major(ch)}")
    print(f"Lowest paying major {lowest_paying_college_major(ch)}")

# paying_major(choice)

# Highest salary by group

group = clean_df.groupby("Group").mean()
print(group.head())

