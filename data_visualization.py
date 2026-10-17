
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the existing dataset
df = pd.read_csv("books_dataset_5_pages.csv")

# Step 2: Make sure Price is numeric
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Price"])

# Step 3: Convert book ratings into numeric values for comparison
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["Rating Numeric"] = df["Rating"].map(rating_map)

# Step 4: Display basic information
print("DATA VISUALIZATION PROJECT")
print("Dataset shape:", df.shape)
print("\nAverage book price:", round(df["Price"].mean(), 2))
print("Minimum book price:", round(df["Price"].min(), 2))
print("Maximum book price:", round(df["Price"].max(), 2))

# Chart 1: Price Distribution Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Book Price")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("chart_1_price_distribution.png", dpi=300)
plt.show()

# Chart 2: Number of Books in Each Price Category
category_order = ["Low", "Medium", "High"]
category_counts = (
    df["Price Category"]
    .value_counts()
    .reindex(category_order, fill_value=0)
)

plt.figure(figsize=(8, 5))
category_counts.plot(kind="bar", edgecolor="black")
plt.title("Number of Books by Price Category")
plt.xlabel("Price Category")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_2_price_categories.png", dpi=300)
plt.show()

# Chart 3: Book Rating Distribution
rating_order = ["One", "Two", "Three", "Four", "Five"]
rating_counts = (
    df["Rating"]
    .value_counts()
    .reindex(rating_order, fill_value=0)
)

plt.figure(figsize=(8, 5))
rating_counts.plot(kind="bar", edgecolor="black")
plt.title("Distribution of Book Ratings")
plt.xlabel("Book Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_3_rating_distribution.png", dpi=300)
plt.show()

# Chart 4: Relationship Between Price and Rating
rating_data = df.dropna(subset=["Rating Numeric"])

plt.figure(figsize=(8, 5))
plt.scatter(rating_data["Price"], rating_data["Rating Numeric"])
plt.title("Relationship Between Book Price and Rating")
plt.xlabel("Book Price")
plt.ylabel("Book Rating (1 = One, 5 = Five)")
plt.yticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig("chart_4_price_vs_rating.png", dpi=300)
plt.show()

# Dashboard: Display four charts together
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

axes[0, 0].hist(df["Price"], bins=10, edgecolor="black")
axes[0, 0].set_title("Book Price Distribution")
axes[0, 0].set_xlabel("Price")
axes[0, 0].set_ylabel("Number of Books")

category_counts.plot(kind="bar", ax=axes[0, 1], edgecolor="black")
axes[0, 1].set_title("Books by Price Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Number of Books")
axes[0, 1].tick_params(axis="x", rotation=0)

rating_counts.plot(kind="bar", ax=axes[1, 0], edgecolor="black")
axes[1, 0].set_title("Book Rating Distribution")
axes[1, 0].set_xlabel("Rating")
axes[1, 0].set_ylabel("Number of Books")
axes[1, 0].tick_params(axis="x", rotation=0)

axes[1, 1].scatter(
    rating_data["Price"],
    rating_data["Rating Numeric"]
)
axes[1, 1].set_title("Price vs Rating")
axes[1, 1].set_xlabel("Book Price")
axes[1, 1].set_ylabel("Rating (1-5)")
axes[1, 1].set_yticks([1, 2, 3, 4, 5])

fig.suptitle("Books Dataset - Data Visualization Dashboard", fontsize=16)
plt.tight_layout()
plt.savefig("books_visualization_dashboard.png", dpi=300)
plt.show()

# Summary for the data story
print("\nPRICE CATEGORY SUMMARY")
print(category_counts)

print("\nRATING SUMMARY")
print(rating_counts)

print("\nPRICE-RATING CORRELATION")
print(
    round(
        rating_data["Price"].corr(rating_data["Rating Numeric"]),
        3
    )
)

print("\nAll charts and the dashboard have been saved.")
