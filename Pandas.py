import matplotlib.pyplot as plt
import numpy as np  # importing numpy
import pandas as pd  # Importing pandas
import seaborn as sns
from matplotlib.ticker import MaxNLocator

df = pd.read_csv(r'C:\Users\Marcos\PycharmProjects\UCDPA_Marcos\Video Games Dataset.csv')  # Loading the csv data set

# Exploring the data set:
print(df.head())  # displays the first few rows
print(df.info())  # displays info on the columns
print(df.shape)  # checks how many rows and columns there are
print(df.describe())  # displays some stats of the data set

# SORTING a NEWLY ADDED COLUMN
df["NonUS_Sales"] = df["Global_Sales"] - df["NorthAmerica_Sales"]  # creates a new column
df_NonUS_Sales = df.sort_values(["NonUS_Sales", "Year"], ascending=[False, True])  # sorts by Non US sales and by year
df_NonUS_Sales_simple = df_NonUS_Sales[["name", "Year", "NonUS_Sales"]]  # Selects the 3 columns we want to display only
print(df_NonUS_Sales_simple.head())

# Creating a boxplot with swarmplot to analyze these Non US Sales
sns.boxplot(data=df_NonUS_Sales, x='Year', y='NonUS_Sales').set(title='Sales in regions other than US')
sns.swarmplot(x="Year", y="NonUS_Sales", data=df_NonUS_Sales, edgecolor="black",alpha=.5, s=1.8,linewidth=0.3)
plt.show()

# GROUPING and sorting
total_sales = df.groupby("Publisher")["Global_Sales"].sum()  # groups by Publisher and the sum of all sales
total_sales_Sorted = total_sales.sort_values(ascending=[False])  # sorts in descending order
print(total_sales_Sorted)

# Plotting a Barplot with grouped sales by Publisher
total_sales = df.groupby("Publisher")["Global_Sales"].sum().reset_index() # let's group this again and reset its index
sns.barplot(x="Global_Sales", y="Publisher", palette="mako", # a more interesting colour palette
            ci = None, # I don't want the error bars displayed
            data=total_sales).set(title="Accumulated Global Sales by Publisher") # adding title
plt.tight_layout()
plt.show()


# GROUPING & NumPy
info_publisher_sales = df.groupby("Publisher")["Global_Sales"]\
    .agg([np.sum, np.max, np.min, np.mean])  # groups by Publisher and shows total sales, max and min, and mean
print(info_publisher_sales)

# SUB-SETTING
df_2010_Nintendo = df[
    (df["Year"] == 2010) & (df["Publisher"] == "Nintendo")]  # select games released in 2010 by Nintendo only
df_2010_Nintendo_simple = df_2010_Nintendo[["name", "Year", "Global_Sales"]]  # selects the columns we want to display

df_2010_Activision = df[
    (df["Year"] == 2010) & (df["Publisher"] == "Activision")]  # select games released in 2010 by Activision only
df_2010_Activision_simple = df_2010_Activision[["name", "Year", "Global_Sales"]]  # selects the columns we want to display

# CREATING A LIST WITH THE SUB-SET
sales_2010 = [["Nintendo", df_2010_Nintendo_simple],
              ["Activision", df_2010_Activision_simple]]
print(sales_2010)

# DROPPING DUPLICATES
unique_games = df.drop_duplicates(subset=["name"])  # removes any duplicated name from the list of games
print(unique_games)

# MERGING DATAFRAMES
df2 = pd.read_csv(r'C:\Users\Marcos\PycharmProjects\UCDPA_Marcos\metacritic_games.csv')  # Loading another csv data set
print(df2.head())

df_df2 = df.merge(df2, on="name")  # Merging two data frames by the word 'name'
print(df_df2.columns)

print(df_df2['Year'].value_counts())  # printing the most popular Year of release within the merged dataframes

print('df_df2 table shape:', df_df2.shape)  # taking a look at the shape of the merge


# COUNT PLOT WITH SEABORN
sns.countplot(y="platform", data=df2).set(title="Titles released per Platform")
plt.show()

# SCATTER PLOT OF MERGED DATAFRAMES WITH HUE AND CUSTOM PALETTE COLOURS
palette_colors = {"Action": "green", "Adventure": "blue",'Shooter': "red", 'Misc': "grey", 'Role-Playing': "brown",
                  'Sports':"pink", 'Platform': "purple", 'Fighting': "black", 'Racing': "orange",
                  'Simulation': "yellow", 'Puzzle': "white"}  # giving colours to categories
sns.scatterplot(x="Year", y="metascore", data=df_df2, hue="Genre",
              palette=palette_colors).set(title="Metascore evolution by genre")
plt.show()

# MATPLOTLIB SCATTER PLOT
N = 20422
x = df2["metascore"]
y = df2['user_score'].astype(float) # Changing so scores are recognized correctly
new_x, new_y = zip(*sorted(zip(x, y)))  # sorting the axis
colors = np.random.rand(N)  # giving a more interesting visual
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(new_x, new_y, c=colors, alpha=0.5)
ax = plt.gca()
ax.yaxis.set_major_locator(MaxNLocator(11))   # reducing the number of points in the Y axis so they are readable
plt.xlabel("Metascore")
plt.ylabel("User Score")
plt.title("Metascore/User Score Scatter Plot")
plt.tight_layout()
plt.show()
