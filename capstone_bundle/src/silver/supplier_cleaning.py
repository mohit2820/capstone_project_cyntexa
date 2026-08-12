from pyspark.sql.functions import col, trim, lower, to_timestamp


def clean_suppliers(df):

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

    # 4. Remove rows where supplier_id is NULL
    df = df.filter(
        col("supplier_id").isNotNull()
    )

    # 5. Convert email to lowercase
    df = df.withColumn(
        "contact_email",
        lower(col("contact_email"))
    )

    # 6.remove null contact_email
    df = df.filter(
        col("contact_email").isNotNull()
    )

    # 7. Remove duplicate supplier IDs
    df = df.dropDuplicates(["supplier_id"])

    # 8.Remove Ingestion Time Col 
    df = df.drop("ingestion_time")

    return df