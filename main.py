import pandas as pd

if __name__ == '__main__':
    df: pd.DataFrame = pd.read_csv("./data/loan_approval_dataset.csv")
    print(df.describe()) 