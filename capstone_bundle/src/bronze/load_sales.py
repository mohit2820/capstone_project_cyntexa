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

for i in range(1000):
    sale_id = i

    customer_id = random.randint(1, 1000)
    product_id = random.randint(1, 1000)

    quantity = random.randint(1, 5)

    price = round(random.uniform(10, 500), 2)

    total_amount = quantity * price

    sale_date = str(fake.date())

    ingestion_time = datetime.now()

    data.append({
        "sale_id": sale_id,
        "customer_id": customer_id,
        "product_id": product_id,
        "quantity": quantity,
        "price": price,
        "total_amount": total_amount,
        "sale_date": sale_date,
        "ingestion_time": ingestion_time
    })

df_sales = pd.DataFrame(data)

df_sales.to_csv("/Volumes/dev/bronze/raw/sales/sales.csv", index=False)

print("Sales CSV saved ✅")