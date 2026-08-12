from pyspark.sql.functions import col, trim, avg, coalesce


def clean_products(product_df, sales_df):

    # 1. Remove duplicate rows
    product_df = product_df.dropDuplicates()

    # 2. Remove extra spaces from string columns
    for column_name, data_type in product_df.dtypes:
        if data_type == "string":
            product_df = product_df.withColumn(
                column_name,
                trim(col(column_name))
            )

    # 3. Convert empty strings to NULL
    product_df = product_df.replace("", None)

    # 4. Remove rows where product_id is NULL
    product_df = product_df.filter(
        col("product_id").isNotNull()
    )

    # 5. Remove rows where supplier_id is NULL
    product_df = product_df.filter(
        col("supplier_id").isNotNull()
    )

    # 6. Convert product price to double
    product_df = product_df.withColumn(
        "price",
        col("price").cast("double")
    )

    # 7. Get price from Sales table
    sales_price = (
        sales_df
        .groupBy("product_id")
        .agg(
            avg("price").alias("sales_price")
        )
    )

    # 8. Join Products with Sales using product_id
    product_df = product_df.join(
        sales_price,
        "product_id",
        "left"
    )

    # 9. If product price is NULL,
    #    use price from Sales
    product_df = product_df.withColumn(
        "price",
        coalesce(
            col("price"),
            col("sales_price")
        )
    )

    # 10. Remove rows where price is still NULL
    product_df = product_df.filter(
        col("price").isNotNull()
    )

    # 11. Remove temporary sales price column
    product_df = product_df.drop("sales_price")

    # 12. Remove duplicate product IDs
    product_df = product_df.dropDuplicates(
        ["product_id"]
    )

    # 13. Remove ingestion time
    product_df = product_df.drop(
        "ingestion_time"
    )

    return product_df