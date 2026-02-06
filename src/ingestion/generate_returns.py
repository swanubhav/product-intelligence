import pandas as pd
import numpy as np

np.random.seed(42)

def generate_returns(orders_path):
    orders = pd.read_csv(orders_path)
    orders["returned"] = np.random.binomial(1, 0.25, size=len(orders))
    return orders[["order_id", "product_id", "returned"]]

if __name__ == "__main__":
    df = generate_returns("data/raw/orders.csv")
    df.to_csv("data/raw/returns.csv", index=False)
    print("Returns data generated")
