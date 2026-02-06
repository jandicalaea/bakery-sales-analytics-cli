# Bakery Sales Analytics CLI (Python + Pandas)

Menu-driven command-line app that loads a one-week bakery sales dataset and produces quick exploratory analysis, week-level KPIs, and product rankings with bar charts.

## Dataset

The included sample file is `data/bread_sales_week.csv` with columns:

- `Date`, `Product`, `Price`, `Cost`, `Quantity`

## Features

- Quick EDA: `head`, `tail`, `describe`, `info`
- Auto-calculated columns (idempotent):
  - `Total Sales = Price × Quantity`
  - `Total Cost = Cost × Quantity`
  - `Profit = Total Sales − Total Cost`
- Weekly KPIs: total sales, total cost, total profit
- Product rankings:
  - Most/least sold (Quantity)
  - Most/least profitable (Profit)
- Bar charts for rankings (Matplotlib)

## Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Run

From the repo root:

```bash
python src/bakery_sales_cli.py
```

Optional flags:

- Use a different CSV:

```bash
python src/bakery_sales_cli.py --csv path/to/your.csv
```

- Save plots to `./outputs` instead of opening a window:

```bash
python src/bakery_sales_cli.py --save-plots
```

## Menu options

1. df.head()
2. df.tail()
3. df.describe()
4. df.info()
5. Total Sales
6. Total Cost
7. Total Profit
8. Most Sold (Quantity + bar chart)
9. Most Profitable (Profit + bar chart)
10. Least Sold (Quantity + bar chart)
11. Least Profitable (Profit + bar chart)
12. Exit

## Project structure

```
.
├─ src/
│  └─ bakery_sales_cli.py
├─ data/
│  └─ bread_sales_week.csv
├─ docs/
│  └─ PandaActivity_Jandicala_Pore.pdf
├─ outputs/               # created/used when --save-plots is enabled
└─ original/
   └─ bread_analysis_original.py
```

## License

MIT (see `LICENSE`).
