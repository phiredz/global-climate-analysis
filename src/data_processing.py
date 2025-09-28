import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    # Drop missing values and duplicate rows
    df = df.dropna().drop_duplicates()
    return df

def merge_datasets(temp_df, co2_df, sea_df):
    # Merge datasets on 'Year'
    merged = temp_df.merge(co2_df, on='Year', how='inner')
    merged = merged.merge(sea_df, on='Year', how='inner')
    return merged
