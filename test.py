import pandas as pd

url_github = 'https://raw.githubusercontent.com/fabiolgc/db-dab-demo/main/data/fe_medium_posts_raw.csv'


pd_df = pd.read_csv(url_github)
spark_df = spark.createDataFrame(pd_df)
