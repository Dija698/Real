import pandas as pd

df = pd.read_csv("Real_Estate_USA.csv")  
print("\n--- 1. DataFrame ---")
print(df)

print("\n--- 2. info() ---")
print(df.info())

print("\n--- dtypes ---")
print(df.dtypes)

print("\n--- describe() ---")
print(df.describe())

print("\n--- shape ---")
print(df.shape)

print("\n--- 3. to_string() basic ---")
print(df.to_string())

print("\n--- to_string(columns subset) ---")
print(df.to_string(columns=["city", "street"]))

print("\n--- to_string(na_rep='MISSING') ---")
print(df.to_string(na_rep="MISSING"))

print("\n--- to_string(float_format) ---")
print(df.to_string(float_format="%.2f".__mod__))

print("\n--- 4. Top 7 rows ---")
print(df.head(7))

print("\n--- 5. Bottom 9 rows ---")
print(df.tail(9))

print("\n--- 6. City column ---")
print(df["city"])
print("\nStreet column ---")
print(df["street"])

print("\n--- 7. Street and City ---")
print(df[["street", "city"]])

print("\n--- 8. Row index 5 ---")
print(df.loc[5])

print("\n--- 9. Rows 3,5,7 ---")
print(df.loc[[3, 5, 7]])

print("\n--- 10. Rows 3 to 9 ---")
print(df.loc[3:9])

print("\n--- 11. Price > 100000 ---")
print(df.loc[df["price"] > 100000])

print("\n--- 12. City == Adjuntas ---")
print(df.loc[df["city"] == "Adjuntas"])

print("\n--- 13. City == Adjuntas & price < 180500 ---")
print(df.loc[(df["city"] == "Adjuntas") & (df["price"] < 180500)])

print("\n--- 14. Row 7, columns city to acre_lot ---")
print(df.loc[7, ["city", "price", "street", "zip_code", "acre_lot"]])

print("\n--- 15. Columns city to zip_code ---")
print(df.loc[:, "city":"zip_code"])

print("\n--- 16. City == Adjuntas, cols city to zip_code ---")
print(df.loc[df["city"] == "Adjuntas", "city":"zip_code"])

print("\n--- 17. 5th row ---")
print(df.iloc[5])

print("\n--- 18. 7th, 9th, 15th row ---")
print(df.iloc[[7, 9, 15]])

print("\n--- 19. Rows 5 to 13 ---")
print(df.iloc[5:14])

print("\n--- 20. 3rd column ---")
print(df.iloc[:, 2])

print("\n--- 21. 2nd, 4th, 7th columns ---")
print(df.iloc[:, [1, 3, 6]])

print("\n--- 22. Columns 2 to 5 ---")
print(df.iloc[:, 1:5])

print("\n--- 23. Rows 7, 9, 15 and Cols 2, 4 ---")
print(df.iloc[[7, 9, 15], [1, 3]])

print("\n--- 24. Rows 2 to 6, Cols 2 to 4 ---")
print(df.iloc[2:7, 1:4])

print("\n--- 25. Add new row ---")
new_row = {"city": "TestCity", "price": 123456, "street": "New St", "zip_code": "12345", "acre_lot": 0.5}
df.loc[len(df)] = new_row
print(df.tail())

print("\n--- 26. Delete row index 2 ---")
df = df.drop(2)
print(df)

print("\n--- 27. Delete rows 4 to 7 ---")
df = df.drop(range(4, 8))
print(df)

print("\n--- 28. Delete 'house_size' column ---")
if "house_size" in df.columns:
    df = df.drop(columns=["house_size"])
print(df)

print("\n--- 29. Delete 'house_size' and 'state' ---")
for col in ["house_size", "state"]:
    if col in df.columns:
        df = df.drop(columns=[col])
print(df)

print("\n--- 30. Rename 'state' to 'state_Changed' ---")
if "state" in df.columns:
    df = df.rename(columns={"state": "state_Changed"})
print(df)

print("\n--- 31. Rename index label from 3 to 5 ---")
df = df.rename(index={3: 5})
print(df)

print("\n--- 32. Query() ---")
print(df.query('price < 127400 and city != "Adjuntas"'))

print("\n--- 33. Sort by price ---")
print(df.sort_values(by="price"))

print("\n--- 34. Group by city, sum price ---")
print(df.groupby("city")["price"].sum())

print("\n--- 35. dropna() ---")
print(df.dropna())

print("\n--- 36. fillna(0) ---")
print(df.fillna(0))
