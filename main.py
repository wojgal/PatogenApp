import streamlit as st
import base64
from data import load_data, create_pdf

st.title('Baza patogenow')

df = load_data()

st.write('Wybierz patogen, aby zobaczyć opis')

options = [f'{row["pathogen_name_pl"]} ({row["pathogen_name_lat"]})' for index, row in df.iterrows()]
options.sort()

selected_option = st.selectbox('Wybierz patogen: ', options, index=None, placeholder='Wybierz patogen')
pdf_buffer = None
create_pdf_button = None

if selected_option:
    polish_name = selected_option.split(' (')[0]
    result = df[df['pathogen_name_pl'] == polish_name].iloc[0]
    
    if result is not None:
        st.write('---')
        st.subheader(f"{result['pathogen_name_pl']} ({result['pathogen_name_lat']})")
        st.write('---')
        st.write('**Opis patogenu:**')
        st.write(result['pathogen_description'])
        st.write('---')
        st.write('**Opis terapii:**')
        st.write(result['therapy_description'])
    
    st.write('---')
    st.download_button(label='Pobierz PDF', data=create_pdf(result['pathogen_name_pl'], result['pathogen_name_lat'], result['pathogen_description'], result['therapy_description']), file_name='raport.pdf', mime='application/pdf')




