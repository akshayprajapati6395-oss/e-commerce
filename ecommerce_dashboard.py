# E-commerce Sales Dashboard using NumPy and pandas
# Install:  pip install numpy pandas
#
# NOTE: This dataset is SYNTHETIC (made up) and created only for
# educational purposes. All seller names are fictional.
import numpy as np
import pandas as pd

PAYMENTS = {"U": "UPI", "C": "Card", "N": "Net Banking", "H": "Cash on Delivery", "W": "Wallet"}
STATUS = {"D": "Delivered", "C": "Cancelled", "R": "Returned"}

# order_id | date | customer | city | seller | category | product | qty | price |
# discount | shipping_fee | payment | status | delivery_days | rating
# (empty value = missing data)
raw = """ORD2001|2026-07-05|CUST11|Delhi|TechZone|Electronics|Wireless Earbuds|1|1999|200|0|U|D|4|4.5
ORD2002|2026-07-12|CUST24|Mumbai|StyleHub|Fashion|Running Shoes|2|2199|400|50|C|D|3|4.2
ORD2003|2026-07-18|CUST07|Bengaluru|HomeNest|Home|Mixer Grinder|1|2999|300|99|N|D|6|3.6
ORD2004|2026-07-21|CUST33|Pune|BookBay|Books|Python Book|2|499|0|40|U|D|2|4.8
ORD2005|2026-07-25|CUST18|Hyderabad|GlowCart|Beauty|Perfume|1|1499|150|50|W|C||
ORD2006|2026-08-02|CUST29|Delhi|TechZone|Electronics|Smart Watch|1|3499|500|0||D|5|4.0
ORD2007|2026-08-06|CUST45|Mumbai|StyleHub|Fashion|Denim Jacket|1|1799|0|50|H|D|7|3.2
ORD2008|2026-08-09|CUST02|Chennai|HomeNest|Home|Table Lamp|3|799|200|60|U|D|4|4.4
ORD2009|2026-08-15|CUST51|Delhi|TechZone|Electronics|Power Bank|2|1299|100|0|C|D|3|
ORD2010|2026-08-19|CUST14|Bengaluru|GlowCart|Beauty|Face Wash|4|299|0|40|U|D|2|4.6
ORD2011|2026-08-23|CUST37|Hyderabad|TechZone|Electronics|Bluetooth Speaker|1|2499|250|0|N|R||
ORD2012|2026-08-28|CUST09|Pune|StyleHub|Fashion|T-Shirt|3|599|100|50|H|D||3.9
ORD2013|2026-09-01|CUST21|Mumbai|BookBay|Books|Notebook Pack|5|249|0|40|W|D|3|4.7
ORD2014|2026-09-04|CUST60|Delhi|HomeNest|Home|Bedsheet Set|2|1299|200|99|C|D|5|4.1
ORD2015|2026-09-08|CUST33|Chennai|StyleHub|Fashion|Backpack|1|1099|0|50|U|D|6|3.5
ORD2016|2026-09-12|CUST16|Bengaluru|TechZone|Electronics|Wireless Earbuds|2|1999|300|0|U|D|2|4.9
ORD2017|2026-09-17|CUST48|Hyderabad|GlowCart|Beauty|Perfume|2|1499|0|50|H|R||
ORD2018|2026-09-20|CUST05|Delhi|BookBay|Books|Python Book|1|499|50|40||D|3|4.5
ORD2019|2026-09-24|CUST27|Mumbai|HomeNest|Home|Mixer Grinder|1|2999|0|99|N|D|8|2.9
ORD2020|2026-09-27|CUST39|Pune|TechZone|Electronics|Smart Watch|2|3499|700|0|W|D|4|4.3
ORD2021|2026-10-02|CUST11|Delhi|StyleHub|Fashion|Running Shoes|1|2199|200|50|U|D|3|4.4
ORD2022|2026-10-05|CUST52|Chennai|GlowCart|Beauty|Face Wash|2|299|0|40|H|C||
ORD2023|2026-10-09|CUST24|Mumbai|TechZone|Electronics|Power Bank|1|1299|0|0|C|D|2|4.6
ORD2024|2026-10-13|CUST43|Bengaluru|HomeNest|Home|Table Lamp|2|799|100|60|U|D|5|3.8
ORD2025|2026-10-17|CUST08|Hyderabad|StyleHub|Fashion|Denim Jacket|2|1799|300|50|W|D|7|3.4
ORD2026|2026-10-21|CUST30|Delhi|TechZone|Electronics|Bluetooth Speaker|2|2499|500|0|U|D||4.2
ORD2027|2026-10-24|CUST19|Pune|BookBay|Books|Notebook Pack|3|249|0|40|H|D|4|4.0
ORD2028|2026-10-27|CUST56|Mumbai|GlowCart|Beauty|Perfume|1|1499|100|50|C|D|3|4.7
ORD2029|2026-10-30|CUST14|Chennai|TechZone|Electronics|Wireless Earbuds|1|1999|0|0|U|D|9|2.8
ORD2030|2026-11-03|CUST41|Delhi|StyleHub|Fashion|T-Shirt|4|599|200|50|U|D|3|4.5
ORD2001|2026-07-05|CUST11|Delhi|TechZone|Electronics|Wireless Earbuds|1|1999|200|0|U|D|4|4.5
ORD2002|2026-07-12|CUST24|Mumbai|StyleHub|Fashion|Running Shoes|2|2199|400|50|C|D|3|4.2"""

# ---------------------------------------------------------------
# 1. Build the DataFrame
# ---------------------------------------------------------------
rows = [line.split("|") for line in raw.strip().split("\n")]
df = pd.DataFrame(rows, columns=["Order_ID", "Order_Date", "Customer_ID", "City", "Seller",
                                 "Category", "Product", "Quantity", "Unit_Price", "Discount",
                                 "Shipping_Fee", "Payment_Method", "Order_Status",
                                 "Delivery_Days", "Customer_Rating"])
df = df.replace("", np.nan)                      # empty text -> missing value
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
for col in ["Quantity", "Unit_Price", "Discount", "Shipping_Fee",
            "Delivery_Days", "Customer_Rating"]:
    df[col] = pd.to_numeric(df[col])
df["Payment_Method"] = df["Payment_Method"].map(PAYMENTS)
df["Order_Status"] = df["Order_Status"].map(STATUS)
df["Order_Value"] = df["Quantity"] * df["Unit_Price"]      # gross value of the order

print("Shape (rows, columns):", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nColumns:", list(df.columns))
print("\nData types:\n", df.dtypes)

# ---------------------------------------------------------------
# 2. Data cleaning
# ---------------------------------------------------------------
print("\n--- Data cleaning ---")
print("Missing values BEFORE:\n", df.isnull().sum())
print("Duplicate orders:", df.duplicated().sum())

df = df.drop_duplicates()                                  # same order counted twice -> remove
df["Payment_Method"] = df["Payment_Method"].fillna("Unknown")

# Delivered orders with missing days/rating -> fill with median.
# (Cancelled/Returned orders have no days or rating, so we leave them empty.)
done = df["Order_Status"] == "Delivered"
for col in ["Delivery_Days", "Customer_Rating"]:
    df.loc[done, col] = df.loc[done, col].fillna(df.loc[done, col].median())

print("Invalid prices   :", (df["Unit_Price"] <= 0).sum())
print("Invalid ratings  :", ((df["Customer_Rating"] < 1) | (df["Customer_Rating"] > 5)).sum())
print("Invalid del. days:", (df["Delivery_Days"] <= 0).sum())
print("Shape AFTER cleaning:", df.shape)

# Extra columns
df["Month"] = df["Order_Date"].dt.strftime("%Y-%m")
df["Day_Type"] = np.where(df["Order_Date"].dt.dayofweek >= 5, "Weekend", "Weekday")

# ASSUMPTIONS for all money calculations:
#  - Only "Delivered" orders count as sales (Cancelled/Returned are NOT sales)
#  - Net value = Order_Value - Discount
#  - Shipping fee is shown separately. None of this is company profit.
sales = df[df["Order_Status"] == "Delivered"].copy()
sales["Net_Value"] = sales["Order_Value"] - sales["Discount"]

# ---------------------------------------------------------------
# 3. NumPy statistics on order value
# ---------------------------------------------------------------
v = sales["Order_Value"].to_numpy()
print("\n--- NumPy statistics (Delivered orders) ---")
print("Mean              :", round(np.mean(v), 2))
print("Median            :", np.median(v))
print("Standard deviation:", round(np.std(v), 2))
print("25th/50th/75th pct:", np.percentile(v, [25, 50, 75]))
print("Min / Max         :", v.min(), "/", v.max())

corr = np.corrcoef(sales["Delivery_Days"].to_numpy(), sales["Customer_Rating"].to_numpy())[0, 1]
print("Correlation (delivery days vs rating):", round(corr, 3))

sales["Value_Category"] = np.select([v >= 5000, v >= 1500], ["High", "Medium"], default="Low")
print("\nOrders per value category:\n", sales["Value_Category"].value_counts())

success = np.mean(df["Order_Status"].to_numpy() == "Delivered") * 100
print("Successful deliveries: {:.1f}%".format(success))

# ---------------------------------------------------------------
# 4. KPI DASHBOARD (main numbers at a glance)
# ---------------------------------------------------------------
total_orders = len(df)
delivered_orders = len(sales)
cancel_rate = (df["Order_Status"] == "Cancelled").mean() * 100
return_rate = (df["Order_Status"] == "Returned").mean() * 100

print("\n" + "=" * 50)
print("          E-COMMERCE KPI DASHBOARD")
print("=" * 50)
print("Total orders (all statuses) :", total_orders)
print("Delivered orders            :", delivered_orders)
print("Gross sales                 : Rs", sales["Order_Value"].sum())
print("Total discounts             : Rs", sales["Discount"].sum())
print("Net sales                   : Rs", sales["Net_Value"].sum())
print("Shipping fees               : Rs", sales["Shipping_Fee"].sum())
print("Average order value         : Rs", round(sales["Order_Value"].mean(), 2))
print("Unique customers            :", df["Customer_ID"].nunique())
print("Cancellation rate           : {:.1f}%".format(cancel_rate))
print("Return rate                 : {:.1f}%".format(return_rate))
print("Average rating              :", round(sales["Customer_Rating"].mean(), 2))
print("Average delivery days       :", round(sales["Delivery_Days"].mean(), 1))
print("=" * 50)

# ---------------------------------------------------------------
# 5. pandas analysis
# ---------------------------------------------------------------
category_orders = df["Category"].value_counts()
print("\n--- Orders by category ---\n", category_orders)

product_orders = df["Product"].value_counts().head(10)
print("\n--- Top 10 products by orders ---\n", product_orders)

seller_summary = (sales.groupby("Seller")
                       .agg(Orders=("Order_ID", "count"),
                            Revenue=("Order_Value", "sum"),
                            Avg_Delivery_Days=("Delivery_Days", "mean"),
                            Avg_Rating=("Customer_Rating", "mean"))
                       .round(2)
                       .sort_values("Revenue", ascending=False))
print("\n--- Seller summary (by revenue) ---\n", seller_summary)

city_summary = (sales.groupby("City")["Order_Value"]
                     .agg(["count", "sum", "mean"]).round(2)
                     .sort_values("sum", ascending=False))
print("\n--- City summary (count, revenue, avg order value) ---\n", city_summary)

payment_orders = df["Payment_Method"].value_counts()
print("\n--- Orders by payment method ---\n", payment_orders)

status_counts = df["Order_Status"].value_counts()
print("\n--- Order status ---\n", status_counts)

category_summary = (sales.groupby("Category")
                         .agg(Orders=("Order_ID", "count"),
                              Revenue=("Order_Value", "sum"),
                              Avg_Rating=("Customer_Rating", "mean"))
                         .round(2).sort_values("Revenue", ascending=False))
print("\n--- Category summary (by revenue) ---\n", category_summary)

monthly_revenue = sales.groupby("Month")["Order_Value"].sum()
print("\n--- Revenue by month ---\n", monthly_revenue)

print("\n--- Weekday vs Weekend orders ---\n", df["Day_Type"].value_counts())

sales["Has_Discount"] = np.where(sales["Discount"] > 0, "With discount", "No discount")
print("\n--- Discount analysis (avg order value) ---\n",
      sales.groupby("Has_Discount")["Order_Value"].mean().round(2))

sales["Delayed"] = sales["Delivery_Days"] > 5
print("\nDelayed deliveries (over 5 days):", sales["Delayed"].sum(), "of", len(sales))

pivot = df.pivot_table(index="Category", columns="Order_Status", values="Order_ID",
                       aggfunc="count", fill_value=0)
print("\n--- Pivot: category x order status ---\n", pivot)

print("\n--- Correlation matrix ---\n",
      sales[["Delivery_Days", "Customer_Rating", "Order_Value"]].corr().round(3))

print("\n--- Top 5 highest-value orders ---\n",
      sales.nlargest(5, "Order_Value")[["Order_ID", "Seller", "City", "Order_Value"]])

# Repeat customers (more than 1 delivered order)
customer_orders = sales["Customer_ID"].value_counts()
repeat_customers = customer_orders[customer_orders > 1]
print("\n--- Repeat customers (2+ delivered orders) ---\n", repeat_customers)

enough = seller_summary[seller_summary["Orders"] >= 2]     # fair comparison: min 2 orders
print("\n--- Lowest-rated sellers (min 2 orders) ---\n", enough.sort_values("Avg_Rating").head(3))

# Search / filter examples
print("\n--- Filtering examples ---")
print("Orders from Delhi    :", len(df[df["City"] == "Delhi"]))
print("Orders above Rs 3000 :", len(df[df["Order_Value"] > 3000]))
print("Rating 4.0 or above  :", ", ".join(seller_summary[seller_summary["Avg_Rating"] >= 4.0].index))
print("Delayed deliveries   :", len(sales[sales["Delayed"]]))
print("Electronics orders   :", len(df[df["Category"] == "Electronics"]))
print("Returned orders      :", len(df[df["Order_Status"] == "Returned"]))

# ---------------------------------------------------------------
# 6. Business insights (all taken from the data above)
# ---------------------------------------------------------------
lost_value = df[df["Order_Status"].isin(["Cancelled", "Returned"])]["Order_Value"].sum()
with_d = sales[sales["Discount"] > 0]["Order_Value"].mean()
no_d = sales[sales["Discount"] == 0]["Order_Value"].mean()
slowest = seller_summary["Avg_Delivery_Days"].idxmax()
if corr < -0.2:
    link = "longer delivery goes with LOWER ratings"
elif corr > 0.2:
    link = "longer delivery goes with HIGHER ratings"
else:
    link = "no strong link"

print("\n--- Business insights ---")
print("1. Most ordered category          :", category_orders.idxmax())
print("2. Highest-revenue category       :", category_summary["Revenue"].idxmax())
print("3. Highest-revenue seller         :", seller_summary["Revenue"].idxmax())
print("4. City with highest sales        :", city_summary["sum"].idxmax())
print("5. Delivery days vs rating        : correlation {:.2f} -> {}".format(corr, link))
print("6. Most popular payment method    :", payment_orders.idxmax())
print("7. Cancelled + returned value (not a sale): Rs", lost_value)
print("8. Avg order value with discount Rs {:.0f} vs without Rs {:.0f}".format(with_d, no_d))
print("9. Slowest seller (needs work)    :", slowest)
print("10. Delivery success rate         : {:.1f}%".format(success))
print("11. Busier day type               :", df["Day_Type"].value_counts().idxmax())

# ---------------------------------------------------------------
# 7. Save results
# ---------------------------------------------------------------
df.to_csv("ecommerce_cleaned.csv", index=False)
seller_summary.to_csv("seller_summary.csv")
category_summary.to_csv("category_summary.csv")
monthly_revenue.to_csv("monthly_revenue.csv")
print("\nSaved ecommerce_cleaned.csv, seller_summary.csv, category_summary.csv")
print("and monthly_revenue.csv")

# ---------------------------------------------------------------
# 8. Search orders by product (type a product name, see its orders)
# ---------------------------------------------------------------
all_products = sorted(df["Product"].unique())
print("\n--- Search orders by product ---")
print("Available products:", ", ".join(all_products))

while True:
    name = input("\nEnter a product name (or type 'exit' to stop): ").strip()
    if name.lower() == "exit":
        print("Search closed. Thank you!")
        break
    if name == "":
        print("Please type a product name.")
        continue

    # case-insensitive search, so "watch" also finds "Smart Watch"
    found = df[df["Product"].str.contains(name, case=False, regex=False, na=False)]

    if found.empty:
        print("No orders found for '" + name + "'. Try one of the available products.")
    else:
        print("\nOrders found for '" + name + "':", len(found))
        print(found[["Order_ID", "Order_Date", "City", "Seller", "Product",
                     "Quantity", "Order_Value", "Order_Status"]].to_string(index=False))
        delivered_found = found[found["Order_Status"] == "Delivered"]
        print("Delivered orders:", len(delivered_found),
              "| Total value of delivered orders: Rs", delivered_found["Order_Value"].sum())
