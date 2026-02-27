import pandas as pd

def clean_financial_data(raw_data):
    df = pd.DataFrame(raw_data)

    # Remove null rows
    df.dropna(how="all", inplace=True)

    # Convert numeric columns
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors="ignore")
        except:
            pass

    return df