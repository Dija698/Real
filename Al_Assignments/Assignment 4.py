import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt

def regression_analysis(X, y, test_size, xlabel, ylabel):
    X = np.array(X).reshape(-1, 1) if len(X.shape) == 1 else np.array(X)
    y = np.array(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    intercept = model.intercept_
    slope = model.coef_
    
    print(f"Intercept: {intercept}")
    print(f"Slope: {slope}")
    
    def predict_value(x_val):
        return intercept + slope * x_val
    
    # Sample predictions
    print("Sample Predictions:")
    for val in X_train[:3]:
        print(f"{xlabel}={val} → Predicted {ylabel}={predict_value(val)}")
    
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    
    print(f"MAE: {mae}")
    print(f"MSE: {mse}")
    print(f"RMSE: {rmse}\n")
    
    return model, X_test, y_test, y_pred

# ========== Task 1 ==========
print("=== Task 1: Real Estate (US) ===")
url1 = "https://raw.githubusercontent.com/ShahzadSarwar10/FULLSTACK-WITH-AI-BOOTCAMP-B1-MonToFri-2.5MonthExplorer/main/DataSetForPractice/Real_Estate_Sales_2001-2022_GL-Short.csv"
df1 = pd.read_csv(url1, index_col="Serial Number")
print(df1)
df1 = pd.read_csv(url1, index_col="Serial Number")

print(df1.dtypes)
print(df1.describe())
print(df1.shape)

regression_analysis(df1["Assessed Value"], df1["Sale Amount"], test_size=0.1,
                    xlabel="Assessed Value", ylabel="Sale Amount")

print("=== Task 2: Zameen.com Real Estate (PK) ===")
url2 = "https://raw.githubusercontent.com/ShahzadSarwar10/FULLSTACK-WITH-AI-BOOTCAMP-B1-MonToFri-2.5MonthExplorer/main/Week2/zameencom-property-data-By-Kaggle-Short.csv"
df2 = pd.read_csv(url2, index_col="property_id")
print(df2)
print(df2.info())
print(df2.dtypes)
print(df2.describe())
print(df2.shape)

regression_analysis(df2["bedrooms"], df2["price"], test_size=0.25,
                    xlabel="Bedrooms", ylabel="Price")

print("=== Task 3: Medical Industry (PK) ===")
url3 = "https://raw.githubusercontent.com/ShahzadSarwar10/FULLSTACK-WITH-AI-BOOTCAMP-B1-MonToFri-2.5MonthExplorer/main/DataSetForPractice/number-of-registered-medical-and-dental-doctors-by-genderin-pakistan%20(1).csv"
df3 = pd.read_csv(url3, index_col="Years")
print(df3)
print(df3.info())
print(df3.dtypes)
print(df3.describe())
print(df3.shape)

regression_analysis(df3["Female Doctors"], df3["Female Dentists"], test_size=0.3,
                    xlabel="Female Doctors", ylabel="Female Dentists")

print("=== Task 4: US Startups (Multiple Linear Regression) ===")
url4 = "https://raw.githubusercontent.com/ShahzadSarwar10/FULLSTACK-WITH-AI-BOOTCAMP-B1-MonToFri-2.5MonthExplorer/main/DataSetForPractice/50_Startups%20(1).csv"
df4 = pd.read_csv(url4)
print(df4)
print(df4.info())
print(df4.dtypes)
print(df4.describe())
print(df4.shape)

X4 = df4.iloc[:, :-1]  
y4 = df4["Profit"]

sns.heatmap(df4.corr(), annot=True, cmap="coolwarm")
plt.show()

model4, X_test4, y_test4, y_pred4 = regression_analysis(X4, y4, test_size=0.1,
                                                        xlabel="Features", ylabel="Profit")

print("=== Task 5: California Housing ===")
url5 = "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/regression_sprint/california_housing.csv"
df5 = pd.read_csv(url5)
print(df5)
print(df5.info())
print(df5.dtypes)
print(df5.describe())
print(df5.shape)

X5 = df5.drop(columns=["median_house_value"])
y5 = df5["median_house_value"]
regression_analysis(X5, y5, test_size=0.1, xlabel="Features", ylabel="Median House Value")

print("=== Task 6: mtcars Dataset ===")
url6 = "https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/regression_sprint/mtcars.csv"
df6 = pd.read_csv(url6)
print(df6)
print(df6.info())
print(df6.dtypes)
print(df6.describe())
print(df6.shape)

X6 = df6.drop(columns=["mpg"])
y6 = df6["mpg"]
regression_analysis(X6, y6, test_size=0.1, xlabel="Features", ylabel="MPG")
