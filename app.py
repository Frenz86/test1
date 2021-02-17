import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def main():
    st.title('Questa è la mia prima webapp!!!')
    df = pd.DataFrame(np.random.randint(0,100,size=(1000,4)),columns=list('ABCD'))
    st.dataframe(df)
    image= Image.open('dog.jpg')
    st.image(image,use_column_width=True)
    st.write('ciao a tutti i miei studenti')
    st.table(df.head())
    lista = ['Email','Telefono Fisso','Cellulare']
    add_selectbox = st.sidebar.selectbox('Come desideri essere contattato?',lista)
    st.sidebar.write(add_selectbox)
    add_slider = st.sidebar.slider('Petal Length',0.0,6.0,0.1)
    st.sidebar.write(add_slider)




if __name__=='__main__':
    main()
