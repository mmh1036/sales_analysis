import pandas as pd 

def load_data():
    df_customers = pd.read_csv("/Users/matthavey/Desktop/bip-python-unh/sales_analysis/data/customers.csv")
    df_contracts = pd.read_csv("/Users/matthavey/Desktop/bip-python-unh/sales_analysis/data/contracts.csv")
    return df_customers,  df_contracts

def combine_data( df_customers,  df_contracts):
    df_customers.rename(columns={'id':'customer_id'}, inplace=True)
    df_customers.set_index('customer_id', inplace=True)
    df_contracts.set_index('customer_id', inplace=True)
    df = df_contracts.join(df_customers, how='left')
    return df