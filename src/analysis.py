def summarize_data(df):
    print("Dataset Overview:")
    print(df.describe())
    print("\nMissing values per column:")
    print(df.isnull().sum())
