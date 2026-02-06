import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "bread_sales_week.csv"
df = pd.read_csv(CSV_FILE)

def ensure_totals():
    """Create Total Sales, Total Cost, Profit if they don't exist yet."""
    if "Total Sales" not in df.columns:
        df["Total Sales"] = df["Price"] * df["Quantity"]
    if "Total Cost" not in df.columns:
        df["Total Cost"] = df["Cost"] * df["Quantity"]
    if "Profit" not in df.columns:
        df["Profit"] = df["Total Sales"] - df["Total Cost"]

def menu():
    print("\nChoose what you want to view:")
    print("1  - df.head()")
    print("2  - df.tail()")
    print("3  - df.describe()")
    print("4  - df.info()")
    print("5  - Show TOTAL SALES (sum of all rows)")
    print("6  - Show TOTAL COST (sum of all rows)")
    print("7  - Show TOTAL PROFIT (sum of all rows)")
    print("8  - MOST SOLD bread (bar graph by Quantity)")
    print("9  - MOST PROFITABLE bread (bar graph by Profit)")
    print("10 - LEAST SOLD bread (bar graph by Quantity)")
    print("11 - LEAST PROFITABLE bread (bar graph by Profit)")
    print("12 - Exit")

while True:
    menu()
    choice = input("Enter choice (1-12): ").strip()

    if choice == "1":
        n = int(input("How many rows? (default 5): ") or 5)
        print(f"\n=== df.head({n}) ===")
        print(df.head(n))

    elif choice == "2":
        n = int(input("How many rows? (default 5): ") or 5)
        print(f"\n=== df.tail({n}) ===")
        print(df.tail(n))

    elif choice == "3":
        print("\n=== df.describe() ===")
        print(df.describe())

    elif choice == "4":
        print("\n=== df.info() ===")
        df.info()

    elif choice == "5":
        ensure_totals()
        total_sales = df["Total Sales"].sum()
        print(f"\n=== TOTAL SALES (₱) ===\n{total_sales:,.2f}")

    elif choice == "6":
        ensure_totals()
        total_cost = df["Total Cost"].sum()
        print(f"\n=== TOTAL COST (₱) ===\n{total_cost:,.2f}")

    elif choice == "7":
        ensure_totals()
        total_profit = df["Profit"].sum()
        print(f"\n=== TOTAL PROFIT (₱) ===\n{total_profit:,.2f}")

    elif choice == "8":
        most_sold = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
        print("\n=== MOST SOLD BREAD (by Quantity) ===")
        print(most_sold)
        most_sold.plot.bar(title="Most Sold Breads by Quantity", ylabel="Pieces", xlabel="Bread", rot=45)
        plt.tight_layout()
        plt.show()

    elif choice == "9":
        ensure_totals()
        most_prof = df.groupby("Product")["Profit"].sum().sort_values(ascending=False)
        print("\n=== MOST PROFITABLE BREAD (₱) ===")
        print(most_prof)
        most_prof.plot.bar(title="Most Profitable Breads", ylabel="Profit (₱)", xlabel="Bread", rot=45)
        plt.tight_layout()
        plt.show()

    elif choice == "10":
        least_sold = df.groupby("Product")["Quantity"].sum().sort_values(ascending=True)
        print("\n=== LEAST SOLD BREAD (by Quantity) ===")
        print(least_sold)
        least_sold.plot.bar(title="Least Sold Breads by Quantity", ylabel="Pieces", xlabel="Bread", rot=45)
        plt.tight_layout()
        plt.show()

    elif choice == "11":
        ensure_totals()
        least_prof = df.groupby("Product")["Profit"].sum().sort_values(ascending=True)
        print("\n=== LEAST PROFITABLE BREAD (₱) ===")
        print(least_prof)
        least_prof.plot.bar(title="Least Profitable Breads", ylabel="Profit (₱)", xlabel="Bread", rot=45)
        plt.tight_layout()
        plt.show()

    elif choice == "12":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please select 1–12.")

