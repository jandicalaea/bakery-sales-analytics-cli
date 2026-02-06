"""Bakery Sales Analytics CLI (Course Project – Data Analytics) — October 2025

A menu-driven command-line application that loads a one-week bakery sales CSV into a
Pandas DataFrame for analysis and visualization.

CSV columns expected:
- Date, Product, Price, Cost, Quantity
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

import pandas as pd
import matplotlib.pyplot as plt


def ensure_totals(df: pd.DataFrame) -> pd.DataFrame:
    """Create Total Sales, Total Cost, Profit columns if missing (idempotent).

    - Total Sales = Price * Quantity
    - Total Cost  = Cost  * Quantity
    - Profit      = Total Sales - Total Cost
    """
    if "Total Sales" not in df.columns:
        df["Total Sales"] = df["Price"] * df["Quantity"]
    if "Total Cost" not in df.columns:
        df["Total Cost"] = df["Cost"] * df["Quantity"]
    if "Profit" not in df.columns:
        df["Profit"] = df["Total Sales"] - df["Total Cost"]
    return df


def print_menu() -> None:
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


def prompt_int(prompt: str, default: int) -> int:
    raw = input(prompt).strip()
    if raw == "":
        return default
    try:
        val = int(raw)
        return val if val > 0 else default
    except ValueError:
        return default


def plot_series(
    series: pd.Series,
    *,
    title: str,
    ylabel: str,
    xlabel: str,
    rotate: int = 45,
    save_dir: Optional[Path] = None,
    filename: Optional[str] = None,
) -> None:
    ax = series.plot.bar(title=title, ylabel=ylabel, xlabel=xlabel, rot=rotate)
    fig = ax.get_figure()
    fig.tight_layout()

    if save_dir and filename:
        save_dir.mkdir(parents=True, exist_ok=True)
        outpath = save_dir / filename
        fig.savefig(outpath, dpi=200)
        print(f"Saved chart to: {outpath}")
        plt.close(fig)
    else:
        plt.show()


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    default_csv = repo_root / "data" / "bread_sales_week.csv"

    parser = argparse.ArgumentParser(description="Bakery Sales Analytics CLI")
    parser.add_argument(
        "--csv",
        type=Path,
        default=default_csv,
        help=f"Path to CSV file (default: {default_csv})",
    )
    parser.add_argument(
        "--save-plots",
        action="store_true",
        help="Save plots to ./outputs instead of opening a window",
    )
    args = parser.parse_args()

    if not args.csv.exists():
        raise FileNotFoundError(
            f"CSV not found: {args.csv}\n"
            "Tip: run from the repo root or pass --csv path/to/your.csv"
        )

    df = pd.read_csv(args.csv)

    while True:
        print_menu()
        choice = input("Enter choice (1-12): ").strip()

        if choice == "1":
            n = prompt_int("How many rows? (default 5): ", 5)
            print(f"\n=== df.head({n}) ===")
            print(df.head(n))

        elif choice == "2":
            n = prompt_int("How many rows? (default 5): ", 5)
            print(f"\n=== df.tail({n}) ===")
            print(df.tail(n))

        elif choice == "3":
            print("\n=== df.describe() ===")
            print(df.describe())

        elif choice == "4":
            print("\n=== df.info() ===")
            df.info()

        elif choice == "5":
            ensure_totals(df)
            total_sales = df["Total Sales"].sum()
            print(f"\n=== TOTAL SALES (₱) ===\n{total_sales:,.2f}")

        elif choice == "6":
            ensure_totals(df)
            total_cost = df["Total Cost"].sum()
            print(f"\n=== TOTAL COST (₱) ===\n{total_cost:,.2f}")

        elif choice == "7":
            ensure_totals(df)
            total_profit = df["Profit"].sum()
            print(f"\n=== TOTAL PROFIT (₱) ===\n{total_profit:,.2f}")

        elif choice == "8":
            most_sold = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
            print("\n=== MOST SOLD BREAD (by Quantity) ===")
            print(most_sold)
            plot_series(
                most_sold,
                title="Most Sold Breads by Quantity",
                ylabel="Pieces",
                xlabel="Bread",
                save_dir=(repo_root / "outputs") if args.save_plots else None,
                filename="most_sold_by_quantity.png" if args.save_plots else None,
            )

        elif choice == "9":
            ensure_totals(df)
            most_prof = df.groupby("Product")["Profit"].sum().sort_values(ascending=False)
            print("\n=== MOST PROFITABLE BREAD (₱) ===")
            print(most_prof)
            plot_series(
                most_prof,
                title="Most Profitable Breads",
                ylabel="Profit (₱)",
                xlabel="Bread",
                save_dir=(repo_root / "outputs") if args.save_plots else None,
                filename="most_profitable_by_profit.png" if args.save_plots else None,
            )

        elif choice == "10":
            least_sold = df.groupby("Product")["Quantity"].sum().sort_values(ascending=True)
            print("\n=== LEAST SOLD BREAD (by Quantity) ===")
            print(least_sold)
            plot_series(
                least_sold,
                title="Least Sold Breads by Quantity",
                ylabel="Pieces",
                xlabel="Bread",
                save_dir=(repo_root / "outputs") if args.save_plots else None,
                filename="least_sold_by_quantity.png" if args.save_plots else None,
            )

        elif choice == "11":
            ensure_totals(df)
            least_prof = df.groupby("Product")["Profit"].sum().sort_values(ascending=True)
            print("\n=== LEAST PROFITABLE BREAD (₱) ===")
            print(least_prof)
            plot_series(
                least_prof,
                title="Least Profitable Breads",
                ylabel="Profit (₱)",
                xlabel="Bread",
                save_dir=(repo_root / "outputs") if args.save_plots else None,
                filename="least_profitable_by_profit.png" if args.save_plots else None,
            )

        elif choice == "12":
            print("Goodbye!")
            return 0

        else:
            print("Invalid choice, please select 1–12.")


if __name__ == "__main__":
    raise SystemExit(main())
