import pandas as pd

def build_return_risk_features():
    orders = pd.read_csv("data/raw/orders.csv")
    returns = pd.read_csv("data/raw/returns.csv")

    df = orders.merge(returns, on=["order_id", "product_id"], how="left")
    df.fillna(0, inplace=True)

    return df

if __name__ == "__main__":
    df = build_return_risk_features()
    df.to_csv("data/processed/return_risk_features.csv", index=False)
    print("Return risk features created")
