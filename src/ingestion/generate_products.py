import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

def generate_products(n=500):
    products = []
    categories = ["Clothing", "Electronics", "Home", "Footwear"]

    for i in range(n):
        launch_date = datetime.now() - timedelta(days=np.random.randint(30, 900))
        products.append({
            "product_id": f"P{i}",
            "category": np.random.choice(categories),
            "price": np.random.randint(500, 5000),
            "launch_date": launch_date,
            "rating_avg": round(np.random.uniform(2.5, 4.8), 2)
        })

    return pd.DataFrame(products)

if __name__ == "__main__":
    df = generate_products()
    df.to_csv("data/raw/products.csv", index=False)
    print("Products data generated")
