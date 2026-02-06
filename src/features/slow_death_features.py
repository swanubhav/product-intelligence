import pandas as pd

def build_slow_death_features():
    products = pd.read_csv("data/raw/products.csv")
    orders = pd.read_csv("data/raw/orders.csv")
    returns = pd.read_csv("data/raw/returns.csv")

    sales = orders.groupby("product_id").size().reset_index(name="sales_count")
    return_rate = returns.groupby("product_id")["returned"].mean().reset_index()

    df = products.merge(sales, on="product_id", how="left")
    df = df.merge(return_rate, on="product_id", how="left")

    df.fillna(0, inplace=True)

    df["product_age_days"] = (
        pd.to_datetime("today") - pd.to_datetime(df["launch_date"])
    ).dt.days

    return df

if __name__ == "__main__":
    df = build_slow_death_features()
    df.to_csv("data/processed/slow_death_features.csv", index=False)
    print("Slow-death features created")
