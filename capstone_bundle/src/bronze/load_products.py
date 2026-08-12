# ✅ Install Faker if not available
try:
    from faker import Faker
except ModuleNotFoundError:
    import subprocess
    subprocess.check_call(["pip", "install", "faker"])
    from faker import Faker

import random
import pandas as pd
from datetime import datetime
data = []

fake = Faker()

categories = ["Electronics", "Clothing", "Home", "Sports"]

for i in range(1000):
    product_id = i if i % 40 != 0 else random.randint(1, 50)  # duplicate ❌

    product_name = fake.word().capitalize() + " " + fake.word().capitalize()

    category = random.choice(categories)

    price = round(random.uniform(10, 500), 2) if i % 12 != 0 else None  # NULL ❌

    supplier_id = random.randint(1, 100)

    ingestion_time = datetime.now()

    data.append({
        "product_id": product_id,
        "product_name": product_name,
        "category": category,
        "price": price,
        "supplier_id": supplier_id,
        "ingestion_time": ingestion_time
    })

df_products = pd.DataFrame(data)

df_products.to_csv("/Volumes/dev/bronze/raw/products/products.csv", index=False)

print("Products CSV saved ✅")