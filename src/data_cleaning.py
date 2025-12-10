import pandas as pd

def clean_data(df):
    # Drop rows with missing customer IDs
    df = df.dropna(subset=["CustomerID"])

    # Convert date column
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Remove negative or invalid quantities
    df = df[df["Quantity"] > 0]

    # Remove negative prices
    df = df[df["UnitPrice"] > 0]

    # Create total amount column
    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

    return df

path = r"C:\Users\dhany\CODING ( END OF ME! )\Retail Customer Segmentation & KPI Dashboard\data\raw\online_retail.csv"
def load_and_clean(path):
    df = pd.read_csv(path, encoding="ISO-8859-1")
    df = clean_data(df)
    return df
