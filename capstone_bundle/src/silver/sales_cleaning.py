from pyspark.sql.functions import col, trim, to_date, to_timestamp


def clean_sales(df):

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

    # 4. Remove rows where sale_id is NULL
    df = df.filter(
        col("sale_id").isNotNull()
    )

    # 5. Remove rows where customer_id is NULL
    df = df.filter(
        col("customer_id").isNotNull()
    )

    # 6. Remove rows where product_id is NULL
    df = df.filter(
        col("product_id").isNotNull()
    )

    # 7. Convert quantity to integer
    df = df.withColumn(
        "quantity",
        col("quantity").cast("int")
    )

    # 8. Convert price to double
    df = df.withColumn(
        "price",
        col("price").cast("double")
    )

    # 9. Convert total_amount to double
    df = df.withColumn(
        "total_amount",
        col("total_amount").cast("double")
    )

    # 10. Convert sale_date to date
    df = df.withColumn(
        "sale_date",
        to_date(col("sale_date"))
    )

    # 11. Remove duplicate sale IDs
    df = df.dropDuplicates(["sale_id"])

    # 12. Remove Ingestion Time Col 
    df = df.drop("ingestion_time")

    return df