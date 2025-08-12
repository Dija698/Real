import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv"  
df = pd.read_csv(url)

print("\n--- Data Info ---")
print(df.info())
print("\n--- Data Types ---")
print(df.dtypes)
print("\n--- Statistical Summary ---")
print(df.describe())
print("\n--- Shape ---")
print(df.shape)

def make_plot(plot_func, x=None, y=None, data=df, title="", filename="", **kwargs):
    plt.figure(figsize=(8, 5))
    plot_func(x=x, y=y, data=data, **kwargs)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

make_plot(sns.lineplot, x="city", y="price", title="City vs Price (Line)", filename="line_city_price.png")
make_plot(sns.lineplot, x="zip_code", y="price", title="Zip Code vs Price (Line)", filename="line_zip_price.png")
make_plot(sns.lineplot, x="City", y="Price", title="City vs Price (Capitalized) (Line)", filename="line_City_Price.png")
make_plot(sns.lineplot, x="year", y="Price", title="Year vs Price (Line)", filename="line_year_Price.png")

make_plot(sns.catplot, x="city", y="price", kind="strip", title="City vs Price (Categorical)", filename="cat_city_price.png")
make_plot(sns.catplot, x="zip_code", y="price", kind="strip", title="Zip Code vs Price (Categorical)", filename="cat_zip_price.png")
make_plot(sns.catplot, x="City", y="Price", kind="strip", title="City vs Price (Capitalized) (Categorical)", filename="cat_City_Price.png")
make_plot(sns.catplot, x="year", y="Price", kind="strip", title="Year vs Price (Categorical)", filename="cat_year_Price.png")

make_plot(sns.kdeplot, x="city", y="price", fill=True, title="City vs Price (KDE)", filename="kde_city_price.png")
make_plot(sns.kdeplot, x="zip_code", y="price", fill=True, title="Zip Code vs Price (KDE)", filename="kde_zip_price.png")
make_plot(sns.kdeplot, x="City", y="Price", fill=True, title="City vs Price (Capitalized) (KDE)", filename="kde_City_Price.png")
make_plot(sns.kdeplot, x="year", y="Price", fill=True, title="Year vs Price (KDE)", filename="kde_year_Price.png")

make_plot(sns.scatterplot, x="city", y="price", title="City vs Price (Scatter)", filename="scatter_city_price.png")
make_plot(sns.scatterplot, x="zip_code", y="price", title="Zip Code vs Price (Scatter)", filename="scatter_zip_price.png")
make_plot(sns.scatterplot, x="City", y="Price", title="City vs Price (Capitalized) (Scatter)", filename="scatter_City_Price.png")
make_plot(sns.scatterplot, x="year", y="Price", title="Year vs Price (Scatter)", filename="scatter_year_Price.png")

make_plot(sns.barplot, x="city", y="price", title="City vs Price (Bar)", filename="bar_city_price.png")
make_plot(sns.barplot, x="zip_code", y="price", title="Zip Code vs Price (Bar)", filename="bar_zip_price.png")
make_plot(sns.barplot, x="City", y="Price", title="City vs Price (Capitalized) (Bar)", filename="bar_City_Price.png")
make_plot(sns.barplot, x="year", y="Price", title="Year vs Price (Bar)", filename="bar_year_Price.png")

plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap_correlation.png")
plt.close()

themes = ["darkgrid", "whitegrid", "dark", "white", "ticks"]
for theme in themes:
    sns.set_theme(style=theme)
    plt.figure(figsize=(8, 5))
    sns.lineplot(x="year", y="Price", data=df)
    plt.title(f"Theme: {theme}")
    plt.tight_layout()
    plt.savefig(f"theme_{theme}.png")
    plt.close()

custom_params = {
    "axes.facecolor": "lightyellow",
    "figure.facecolor": "lightblue",
    "axes.grid": True
}
sns.set_theme(style="whitegrid", rc=custom_params)
plt.figure(figsize=(8, 5))
sns.lineplot(x="year", y="Price", data=df)
plt.title("Custom Theme")
plt.tight_layout()
plt.savefig("theme_custom.png")
plt.close()

print("✅ All tasks completed. Plots saved as PNG files.")
