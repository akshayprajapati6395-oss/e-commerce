# E-commerce Sales Dashboard (NumPy + pandas)

Ek beginner-friendly data analysis project jo NumPy aur pandas se e-commerce orders ka data clean karta hai, KPI dashboard banata hai aur business insights nikalta hai.

> **Note:** Dataset **synthetic (made-up)** hai aur sirf educational purpose ke liye banaya gaya hai. Saare seller names fictional hain.

## Project Files

| File | Description |
|------|-------------|
| `ecommerce_dashboard.py` | Main Python script (cleaning + KPI dashboard + analysis + insights + product search) |
| `ecommerce_cleaned.csv` | Cleaned dataset (duplicates removed, missing values handled) |
| `requirements.txt` | Required Python libraries |
| `README.md` | Project documentation |

## Installation

```bash
pip install -r requirements.txt
```

## Run kaise kare

```bash
python ecommerce_dashboard.py
```

Script ke end me ek interactive search aata hai: product ka naam type karo (jaise `watch`) aur uske orders dikhenge. Band karne ke liye `exit` type karo.

## Script kya karti hai

1. **DataFrame banana** - raw text data ko pandas DataFrame me convert karna, codes (`U`, `D`, `R`...) ko full names me map karna.
2. **Data cleaning** - duplicate orders hatana, missing payment method ko `Unknown` karna, delivered orders ke missing delivery days/rating ko median se fill karna, invalid values check karna.
3. **NumPy statistics** - mean, median, standard deviation, percentiles, correlation (delivery days vs rating), value category (Low/Medium/High).
4. **KPI dashboard** - total orders, gross/net sales, average order value, unique customers, cancellation rate, return rate, average rating, average delivery days.
5. **pandas analysis** - category, seller, city, payment method, month, weekday/weekend ke hisaab se summary, discount analysis, delayed deliveries, pivot table, repeat customers.
6. **Business insights** - 11 insights jaise top category, highest-revenue seller, delivery success rate, slowest seller.
7. **Save results** - cleaned data aur summary CSV files save karna.
8. **Product search** - product name se orders search karna.

## Assumptions

- Sirf **Delivered** orders ko sales mana gaya hai (Cancelled/Returned sales nahi hain).
- Net value = Order value - Discount.
- Shipping fee alag se dikhayi gayi hai; ye company ka profit nahi hai.
- Delayed delivery = 5 din se zyada.
- Value category: High = Rs 5000 ya zyada, Medium = Rs 1500 ya zyada, baaki Low.

## Output Files

Script chalane par ye CSV files banti hain:

- `ecommerce_cleaned.csv`
- `seller_summary.csv`
- `category_summary.csv`
- `monthly_revenue.csv`

## Tech Stack

- Python 3
- NumPy
- pandas
