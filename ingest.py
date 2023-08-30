from os import path

import dlt
from pyspark.sql import DataFrame
from pyspark.sql.functions import regexp_replace
import pandas as pd

@dlt.table
@dlt.expect("No null links", "link is not null")
def medium_raw():
    csv_path = 'https://raw.githubusercontent.com/fabiolgc/db-dab-demo/main/data/fe_medium_posts_raw.csv'
    #csv_path = "dbfs:/data-asset-bundles-dais2023/fe_medium_posts_raw.csv"
    pd_df = pd.read_csv(csv_path)
    spark_df = spark.createDataFrame(pd_df)
    #return spark.read.csv(csv_path, header=True)
    return spark_df


@dlt.table
def medium_clean():
    df: DataFrame = dlt.read("medium_raw")
    df = df.filter(df.link != 'null')
    df = df.withColumn("author", regexp_replace("author", "\\([^()]*\\)", ""))
    return df
