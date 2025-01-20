import streamlit as st
import base64
from data import load_data, create_pdf

st.title('Baza patogenow')

df = load_data()

st.write('Wybierz patogen, aby zobaczyć opis')

options = [f'{row["pathogen_name_pl"]} ({row["pathogen_name_lat"]})' for index, row in df.iterrows()]
options.sort()

selected_option = st.selectbox('Wybierz patogen: ', options, index=None, placeholder='Wybierz patogen')
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
    create_pdf_button = st.button('Generuj PDF')

if create_pdf_button:
    pdf_buffer = create_pdf(result['pathogen_name_pl'], result['pathogen_name_lat'], result['pathogen_description'], result['therapy_description'])

    pdf_base64 = base64.b64encode(pdf_buffer.read()).decode('utf-8')
    pdf_buffer.seek(0)

    pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)




