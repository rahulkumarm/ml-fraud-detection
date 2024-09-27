import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    # Drop unnecessary columns
    df = df.drop(columns=['Transaction ID', 'Date', 'Description'])

    # Fill missing values
    df.fillna(0, inplace=True)

    # Label encoding categorical features
    label_encoder = LabelEncoder()
    df['Merchant'] = label_encoder.fit_transform(df['Merchant'])
    df['Category'] = label_encoder.fit_transform(df['Category'])

    # Normalize the 'Amount' feature
    df['Amount'] = (df['Amount'] - df['Amount'].min()) / (df['Amount'].max() - df['Amount'].min())
    
    return df