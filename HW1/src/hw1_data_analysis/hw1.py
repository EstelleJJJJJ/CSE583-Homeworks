
# %% 1
from pathlib import Path
import pandas as pd

data_path = Path(__file__).parent / "bicycle_data.csv"
df = pd.read_csv(data_path)
print(df.head())



# %% Inspect columns
# the three columns represents the # of bicycles
print(df.columns.tolist())
print(df.head())

# %% 2

print("Original data types:")
print(df.dtypes)

# The Date column initially has the object data type because its values
# are stored as text. It should be converted to datetime.
#
# Total, West Sidewalk, and East Sidewalk columns initially have
# the float64 data type. 
# Bicycle counts should be whole numbers, so changing remaining three columns to 
# nullable Int64 is more appropriate.

#change to datetime type 
df["Date"] = pd.to_datetime(
    df["Date"],
    format="%m/%d/%Y %I:%M:%S %p",
)

count_columns = df.columns[1:]
df[count_columns] = df[count_columns].astype("Int64")

print("\nUpdated data types:")
print(df.dtypes)

# %% 3
west_column = (
    "Fremont Bridge Sidewalks, south of N 34th St "
    "Cyclist West Sidewalk"
)
east_column = (
    "Fremont Bridge Sidewalks, south of N 34th St "
    "Cyclist East Sidewalk"
)

df["Total"] = df[west_column] + df[east_column]
df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year

print(df[["Date", west_column, east_column, "Total", "Hour", "Year"]].head())


# %% 4
df_2016 = df[df["Year"] == 2016].copy()

print(df_2016.head())
print("Number of rows:", len(df_2016))
# 366 * 24
print("Years included:", df_2016["Year"].unique())

#%%5 
# %% 5
missing_by_column = df_2016.isna().sum()
missing_time_points = df_2016.isna().any(axis=1).sum()

print("Missing values by column:")
print(missing_by_column)

print("\nNumber of time points with missing data:")
print(missing_time_points)

print("\nRows with missing data:")
print(df_2016[df_2016.isna().any(axis=1)])

# There is 1 time point with missing data in the 2016 dataset: 2016-03-13 02:00:00.
# This row is removed so it will not affect further questions.
df_2016_clean = df_2016.dropna(subset=["Total"]).copy()

print("\nRows before removing missing data:", len(df_2016))
print("Rows after removing missing data:", len(df_2016_clean))


# %% 6
# %% 6
import matplotlib.pyplot as plt

counts_by_hour = df_2016_clean.groupby("Hour")["Total"].sum()

plt.figure(figsize=(10, 6))
plt.plot(
    counts_by_hour.index,
    counts_by_hour.values,
    marker="o",
)

plt.title("Fremont Bridge Bicycle Counts by Hour in 2016")
plt.xlabel("Hour of the Day")
plt.ylabel("Total Bicycle Count")
plt.xticks(range(24))
plt.grid(alpha=0.3)
plt.tight_layout()

output_path = Path(__file__).parents[2] / "counts_by_hour.png"
plt.savefig(output_path, dpi=300)
plt.show()

print("Plot saved to:", output_path)

# %% 7 
# %% 7
average_by_hour = df_2016_clean.groupby("Hour")["Total"].mean()

busiest_hour = average_by_hour.idxmax()
busiest_average = average_by_hour.max()

# On average, the busiest hour of the day was 17:00 (5:00 PM).
print("Busiest hour:", busiest_hour)
print("Average bicycle count:", busiest_average)

# 5PM is the busiest hour during the day. 
