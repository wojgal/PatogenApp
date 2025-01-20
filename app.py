import streamlit as st
from data import load_data

st.title('Baza patogenow')

df = load_data()

st.write('Wybierz patogen, aby zobaczyć opis')

pathogen_list = df['patogen'].tolist()
pathogen_list = sorted(pathogen_list)

selected_pathogen = st.selectbox('Patogen: ', pathogen_list)

opis = df.loc[df['patogen'] == selected_pathogen, 'opis'].values[0]

st.write('### Opis')
st.write(opis)


