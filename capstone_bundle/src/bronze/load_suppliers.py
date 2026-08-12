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
    supplier_id = i if i % 20 != 0 else random.randint(1, 30)  # duplicate ❌

    supplier_name = fake.company()

    city = fake.city()
    state = fake.state_abbr()

    contact_email = fake.email() if i % 8 != 0 else None  # NULL ❌

    ingestion_time = datetime.now()

    data.append({
        "supplier_id": supplier_id,
        "supplier_name": supplier_name,
        "city": city,
        "state": state,
        "contact_email": contact_email,
        "ingestion_time": ingestion_time
    })

df_suppliers = pd.DataFrame(data)

df_suppliers.to_csv("/Volumes/dev/bronze/raw/suppliers/suppliers.csv", index=False)

print("Suppliers CSV saved ✅")