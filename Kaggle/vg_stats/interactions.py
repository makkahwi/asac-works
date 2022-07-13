from vg_stats.vg_stats import nump, panda

# Import Data
df = panda.read_csv("../input/videogames-sales-dataset/PS4_GamesSales.csv")
df

# Check Data Importing
df.head(5)

# Check Info
df.info()

# Check Data Types
df.dtypes

# Most Popular Publisher
publisher = df.Publisher.value_counts().idxmax()
publisher

# Most Popular Platform
platform = df["Platform"].mode()[0]
platform

# Most Popular Genre
genre = df["Genre"].mode()[0]
genre

# Highest Grossing
grossing = df["Name"].head(20)
grossing

# north america median
north_america = df["NA_Sales"]
na_median = north_america.median()
na_median

# north america median ten games
na = df[north_america == 0.08].head(10)
na

# Top selling game
top_game = df.iloc[0]
top_game

# Average number of Nintendo Wii games sales compare with all of the other platforms
avg_sales = (
    df.groupby("Platform").mean()["Global_Sales"].sort_values(ascending=False).head(10)
)
avg_sales["Wii"]

# Platforms List
def unique(org_list):
    list = []

    for x in org_list:
        if x not in list:
            list.append(x)

    return list


common_platforms = unique(df["Platform"])
common_platforms

# Top Selling Action Game
action = df[df["Genre"] == "Action"].head(1)
action.Name

# Top Sales In EU & North America
df["Total"] = df["EU_Sales"] + df["NA_Sales"]
df.head(5)
