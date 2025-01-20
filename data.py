import pandas as pd
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import io

def load_data(csv_path='data/patogeny.csv'):
    try:
        df = pd.read_csv(csv_path)
        return df
    
    except FileNotFoundError:
        st.error(f'Plik {csv_path} z danymi nie istnieje.')
        return None
    
def create_pdf(pathogen_name_pl, pathogen_name_lat, pathogen_description, therapy_description):
    buffer = io.BytesIO()
    document = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph(pathogen_name_pl, styles['BodyText']))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(pathogen_name_lat, styles['BodyText']))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(pathogen_description, styles['BodyText']))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(therapy_description, styles['BodyText']))

    document.build(elements)
    buffer.seek(0)

    return buffer
