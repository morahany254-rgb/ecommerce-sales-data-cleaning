import pandas as pd

# تحميل الملف
df = pd.read_excel("G:\\Project\\ecommerce_messy_data.xlsx")
# قمت بأخذ نسخه من البيانات
data = df.copy()
# كنت بشوف طبيعو البيانات ونوعها
print(data.head(10))
print(data.info())
# معرفة عدد العواميد والصفوف
print(data.shape)

# معرفة أسماء العواميد
print(data.columns)

# تعديل عمود ID
data = data.dropna(subset="Order ID")
data["Order ID"] = pd.to_numeric(data["Order ID"], errors="coerce").astype("Int16")

# تعديل عمود Customer Name & Category & Payment Method & City
for loc in data[["Customer Name", "Category", "Payment Method", "City"]]:
    data[loc] = data[loc].astype(str).str.strip().str.title().fillna("unknown")

# تعديل عمود Quantity
data["Quantity"] = (
    data["Quantity"].astype(str).str.strip().str.replace("two", "2", regex=True)
)
data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce").astype("Int16")
data = data[data["Quantity"] > 0]

# print(data.info())

# تعديل عمود Unit Price
data["Unit Price"] = (
    data["Unit Price"]
    .astype(str)
    .str.strip()
    .str.replace(r"EGP|\$|,", "", regex=True)
    .str.replace("invalid_price", "0", regex=True)
)
data = data.dropna(subset="Unit Price")
data["Unit Price"] = pd.to_numeric(data["Unit Price"], errors="coerce").astype(
    "Float64"
)
data = data[data["Unit Price"] > 0]


# تعديل عمود Discount

data["Discount"] = (
    data["Discount"]
    .astype(str)
    .str.strip()
    .str.replace("20%", "0.2", regex=True)
    .str.replace("5%", "0.05", regex=True)
    .fillna("0")
)
data["Discount"] = pd.to_numeric(data["Discount"], errors="coerce").astype("Float32")
# تعديل عمود Order Date

data["Order Date"] = (
    data["Order Date"].astype(str).str.strip().replace(r"\.|/", "-", regex=True)
)

data["Order Date"] = pd.to_datetime(data["Order Date"], errors="coerce", format="mixed")

# أضافة عمود جديد أجمالى السعر
data["Total price"] = data["Quantity"] * data["Unit Price"] * (1 - data["Discount"])
# أعادة ترتيب الأعمده
Rearranging_the_columns = [
    "Order ID",
    "Customer Name",
    "Category",
    "Order Date",
    "Quantity",
    "Unit Price",
    "Discount",
    "Total price",
    "Payment Method",
    "City",
]
data = data.reindex(columns=Rearranging_the_columns)
data = data.reset_index(drop=True)
# تصدير الملف
data.to_excel("ecommerce_cleaned_data.xlsx", index=False)
