import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time




st.set_page_config(
    page_title="Demo-Data Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

new_title1 = '<p style="font-family:sans-serif; color:Blue; font-size: 42px;">🎲 My Demo Application</p>'
st.markdown(new_title1, unsafe_allow_html=True)
# st.markdown("### 🎲 My Demo Application")

st.title('File uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)


    new_title2 = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">**♟ DataFrame ♟**</p>'
    st.markdown(new_title2, unsafe_allow_html=True)
    # st.markdown('**♟ DataFrame ♟**')

    def highlight_percentage(s):
        if s.Percentage>=90:
            row_color = ['background-color: ForestGreen']*len(s)
        elif s.Percentage<30:
            row_color = ['background-color: red']*len(s)
        else: 
            row_color = ['background-color: AntiqueWhite']*len(s)

        return row_color

    st.dataframe(df.style.apply(highlight_percentage, axis=1))

    # st.write(df)
    #st.markdown('**♟ Descriptive Statistics ♟**')
    #st.write(df.describe())

    new_title3 = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">visualization</p>'
    st.markdown(new_title3, unsafe_allow_html=True)
    # st.title('visualization')

    st.subheader('Click any button')

    tab1, tab2 = st.tabs(["Line Chart", "Bar Chart"])

    with tab1:
        st.header("Line chart visualization")
        st.line_chart(df, x='Name', y=['Percentage', 'Python Marks', 'Azure Marks', 'CSS Marks'])
    with tab2:
        st.header("Bar chart Name vs Percentage")
        st.bar_chart(df, y=['Python Marks', 'Azure Marks', 'CSS Marks'], x='Name')

    # if st.button('Line Chart'): 
    #     st.write('Line chart visualization')
    #     st.line_chart(df)
    # if st.button('Bar Chart'):
    #     st.write('Bar Chart visualization')
    #     st.bar_chart(df)

else:
  st.info('☝️ Upload a CSV file')





