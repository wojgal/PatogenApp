import pandas as pd
import streamlit as st

def load_data(csv_path='data/patogeny.csv'):
    try:
        df = pd.read_csv(csv_path)
        return df
    
    except FileNotFoundError:
        st.error(f'Plik {csv_path} z danymi nie istnieje.')
        return None