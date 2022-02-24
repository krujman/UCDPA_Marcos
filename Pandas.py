import pandas as pd  # Importing pandas
import numpy as np  # importing numpy

df = pd.read_csv(r'C:\Users\Marcos\PycharmProjects\UCDPA_Marcos\Video Games Dataset.csv')  # Loading the csv data set

# Exploring the data set:
print(df.head())  # displays the first few rows
print(df.info())  # displays info on the columns
print(df.shape)  # checks how many rows and columns there are
print(df.describe())  # displays some stats of the data set

# SORTING a NEWLY ADDED COLUMN
df["NonUS_Sales"] = df["Global_Sales"] - df["NorthAmerica_Sales"]  # creates a new column
df_NonUS_Sales = df.sort_values(["NonUS_Sales", "Year"], ascending=[False, True])  # sorts by Non US sales and by year
df_NonUS_Sales_simple = df_NonUS_Sales[["Name", "Year", "NonUS_Sales"]]  # Selects the 3 columns we want to display only
print(df_NonUS_Sales_simple.head())

# GROUPING
total_sales = df.groupby("Publisher")["Global_Sales"].sum()  # groups by Publisher and the sum of all sales
total_sales_Sorted = total_sales.sort_values(ascending=[False])  # sorts in descending order
print(total_sales_Sorted)

# GROUPING & NumPy
info_publisher_sales = df.groupby("Publisher")["Global_Sales"]\
    .agg([np.sum, np.max, np.min, np.mean])  # groups by Publisher and shows total sales, max and min, and mean
print(info_publisher_sales)

# SUB-SETTING
df_2010_Nintendo = df[
    (df["Year"] == 2010) & (df["Publisher"] == "Nintendo")]  # select games released in 2010 by Nintendo only
df_2010_Nintendo_simple = df_2010_Nintendo[["Name", "Year", "Global_Sales"]]  # selects the columns we want to display
print(df_2010_Nintendo_simple)

# DROPPING DUPLICATES
unique_games = df.drop_duplicates(subset=["Name"])  # removes any duplicated name from the list of games
print(unique_games)

