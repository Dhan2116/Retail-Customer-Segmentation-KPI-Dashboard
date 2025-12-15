import pandas as pd

def get_cluster_summary(df, features):
    summary = df.groupby("Cluster")[features].mean().round(2)
    counts = df["Cluster"].value_counts().rename("NumCustomers")
    summary = summary.join(counts)
    return summary.sort_index()
