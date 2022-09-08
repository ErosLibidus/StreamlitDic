import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu
import psycopg2
from creden import HOST, DATABASE, USER_BASE, PASSWORD_BASE
import os 
import xlrd
import openpyxl
def consultas2(consulta):
    try:
        connetion = psycopg2.connect(host=HOST, dbname=DATABASE, user=USER_BASE, password=PASSWORD_BASE)
        micursor = connetion.cursor()
        micursor.execute(consulta)
        column_names = [desc[0] for desc in micursor.description]
        df = micursor.fetchall()
        df = list(df)
        df = pd.DataFrame(df)
        n=0
        for i in df.columns:
            df.rename(columns={i:column_names[n]}, inplace=True)
            n+=1
        return df  
    except Exception as error:
        print(error)
    finally:
        if micursor is not None:
            micursor.close()
        if connetion is not None:
            connetion.close()
        #return df  
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
with st.sidebar:
    choose = option_menu("Galeria", ["Inicio", "Diccionarios"],
                        icons=['house', "house"],
                        menu_icon="app-indicator", default_index=0,
                        styles={
        "container": {"padding": "8!important", "background-color": "#202022"},
        "icon": {"color": "#00747C", "font-size": "15px"}, 
        "nav-link": {"font-size": "18px", "text-align": "down", "margin":"0px", "--hover-color": "#363333"},
        "nav-link-selected": {"background-color": "#579DFF"},
    }
    )


if choose == "Inicio":
    try:
        text = st.text_area('Consulta SQL')
        #consultas2(text)
        df = consultas2(text)
        capbutton = st.button("consultar")
        if capbutton:
            st.table(df.head(10))
            df.to_csv(index=False).encode("utf-8")
            csv = convert_df(df)
        text2 = st.text_input("Nombre de archivo")
        csv=df.to_csv()
        st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name=text2 + ".csv",
        mime='text/csv',
    )

    except:
        
        st.write("La consulta no es correcta")


if choose == "Diccionarios":
    # df = consultas2("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
    # df = pd.DataFrame(df)
    # nom = tuple(df["tablename"])
    # ini = st.selectbox("Elegir tabla", options=nom)
    # f = open("energy.md", "r")

    tabla = pd.read_csv("archivos/Diccionario-final.csv")
    nom = tuple(tabla["Entidad"].unique())
    ini = st.selectbox("Elegir tabla", options=nom)
    for i in tabla["Entidad"].unique():
        if ini == i:
            st.write(tabla[tabla["Entidad"] == i])
            #break
            #st.write(f.read())


    #st.table(tabla[tabla["Entidad"] == "tabla_hecho"])
    #st.write(f.read())
    #x = xlrd.open_workbook_xls("Diccionario-de-Datos.xlsx")}
    #ex = pd.read_excel("Diccionario-de-Datos.xlsx")
    #ex.to_csv("caca.csv")
    #st.write(ex)
