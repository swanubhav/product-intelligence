import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

def generate_orders(n=5000):
    orders = []

    for i in range(n):
        orders.append({
            "order_id": f"O{i}",
            "product_id": f"P{np.random.randint(0,500)}",
            "user_id": f"U{np.random.randint(0,1000)}",
            "order_date": datetime.now() - timedelta(days=np.random.randint(1, 365)),
            "quantity": np.random.randint(1, 3)
        })

    return pd.DataFrame(orders)

if __name__ == "__main__":
    df = generate_orders()
    df.to_csv("data/raw/orders.csv", index=False)
    print("Orders data generated")
