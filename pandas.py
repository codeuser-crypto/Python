import pandas as pd
data1 = pd.DataFrame({"Name": ["John", "Alice", "Bob"], "Age": [25, 24, 26]})
data2 = pd.DataFrame({"City": ["London", "NYC", "Paris"], "Population": [8_000_000, 8_500_000, 2_000_000]})
with pd.ExcelWriter("multisheet.xlsx") as writer:
    data1.to_excel(writer, sheet_name = "people", index = False)
    data2.to_excel(writer, sheet_name = "cities", index = False)
print("Excel file with mutliple sheets created successfully")
