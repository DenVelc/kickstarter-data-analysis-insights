import pandas as pd

# Load dataset
df = pd.read_csv("kickstarter_projects.csv", parse_dates=["Launched", "Deadline"])

# Clean data
df = df[df["State"].isin(["Successful", "Failed", "Canceled", "Live", "Suspended"])]
df = df[df["Goal"] > 0]
df["Goal_Completion_Percent"] = (df["Pledged"] / df["Goal"]) * 100
df["Launch_Year"] = df["Launched"].dt.year
df["Campaign_Length"] = (df["Deadline"] - df["Launched"]).dt.days

# 1. Success rate by category
success_by_category = (
    df[df["State"] == "Successful"]
    .groupby("Category")
    .size()
    .div(df.groupby("Category").size()) * 100
).sort_values(ascending=False)

# 2. Average pledged amount by category
avg_pledged_by_cat = df.groupby("Category")["Pledged"].mean().sort_values(ascending=False)

# 3. Average number of backers by category
avg_backers_by_cat = df.groupby("Category")["Backers"].mean().sort_values(ascending=False)

# 4. Top project by goal completion percentage (for goals over $1000)
top_project = df[df["Goal"] > 1000].sort_values("Goal_Completion_Percent", ascending=False).head(1)

# 5. Number of projects by launch year
projects_by_year = df["Launch_Year"].value_counts().sort_index()

# 6. Success rate trend over time
success_trend = (
    df[df["State"].isin(["Successful", "Failed"])]
    .groupby(["Launch_Year", "State"])
    .size()
    .unstack()
)
success_trend["Success_Rate_%"] = success_trend["Successful"] / (success_trend["Successful"] + success_trend["Failed"]) * 100

# 7. Average campaign length by project state
avg_campaign_length = df.groupby("State")["Campaign_Length"].mean()

# 8. Median goal amount by project state
median_goal_by_state = df.groupby("State")["Goal"].median()

# 9. Top countries by number of projects
top_countries = df["Country"].value_counts().head(10)

# 10. Median goal completion % by category
goal_completion_by_cat = (
    df[df["State"] == "Successful"]
    .groupby("Category")["Goal_Completion_Percent"]
    .median()
    .sort_values(ascending=False)
)

# Print outputs
print("\n--- Success Rate by Category (Top 5) ---\n", success_by_category.head(5))
print("\n--- Average Pledged Amount by Category (Top 5) ---\n", avg_pledged_by_cat.head(5))
print("\n--- Average Number of Backers by Category (Top 5) ---\n", avg_backers_by_cat.head(5))
print("\n--- Top Project by Goal Completion Percentage (Goal > $1000) ---\n", top_project[["Name", "Category", "Goal", "Pledged", "Goal_Completion_Percent"]])
print("\n--- Number of Projects Launched per Year ---\n", projects_by_year)
print("\n--- Success Rate Trend Over the Years (%) ---\n", success_trend["Success_Rate_%"])
print("\n--- Average Campaign Length by Project State (Days) ---\n", avg_campaign_length)
print("\n--- Median Goal Amount by Project State (USD) ---\n", median_goal_by_state)
print("\n--- Top 10 Countries by Number of Projects ---\n", top_countries)
print("\n--- Median Goal Completion Percentage by Category (Top 5) ---\n", goal_completion_by_cat.head(5))
