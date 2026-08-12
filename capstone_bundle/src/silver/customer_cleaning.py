from pyspark.sql.functions import col, trim, lower, to_date


def clean_customers(df):
    # 1. Remove duplicate rows
    df = df.dropDuplicates()

    # 2. Remove extra spaces from string columns
    for column_name, data_type in df.dtypes:
        if data_type == "string":
            df = df.withColumn(
                column_name,
                trim(col(column_name))
            )

    # 3. Convert empty strings to NULL
    df = df.replace("", None)

    # 4. Remove rows where customer_id is NULL
    df = df.filter(
        col("customer_id").isNotNull()
    )

    # 5. Remove rows where email is NULL
    df = df.filter(
        col("email").isNotNull()
    )

    # 6. Remove rows where phone is NULL
    df = df.filter(
        col("phone").isNotNull()
    )

    # 7. Convert email to lowercase
    df = df.withColumn(
        "email",
        lower(col("email"))
    )

    # 8. Convert signup_date to DATE
    df = df.withColumn(
        "signup_date",
        to_date(col("signup_date"))
    )

    # 9. Remove duplicate customer IDs
    df = df.dropDuplicates(["customer_id"])

    # 10.Remove Ingestion Time Col 
    df = df.drop("ingestion_time")

    return df