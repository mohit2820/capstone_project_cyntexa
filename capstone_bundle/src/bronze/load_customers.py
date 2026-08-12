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

fake = Faker()

data = []

for i in range(1000):
    customer_id = i if i % 50 != 0 else random.randint(1, 20)  # duplicate ❌

    name = fake.name()

    email = fake.email() if i % 10 != 0 else None  # NULL ❌

    city = fake.city()
    state = fake.state_abbr()

    signup_date = str(fake.date())

    phone = fake.phone_number() if i % 15 != 0 else None  # NULL ❌

    ingestion_time = datetime.now()  # same as Spark current_timestamp()

    data.append({
        "customer_id": customer_id,
        "name": name,
        "email": email,
        "city": city,
        "state": state,
        "signup_date": signup_date,
        "phone": phone,
        "ingestion_time": ingestion_time
    })

# ✅ Create Pandas DataFrame
df = pd.DataFrame(data)

# ✅ Save as CSV (single file)
output_path = "/Volumes/dev/bronze/raw/customers/customers.csv"
df.to_csv(output_path, index=False)

print("CSV saved at:", output_path)