import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

# from snowflake.connector import connect
# from snowflake.connector.connection import SnowflakeConnection
import snowflake.connector


# Page configuration
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

# Connect to snowflake and fetch data
# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

if st.button('Snowflake'): 
    rows = run_query("SELECT * from data;")
    # df1 = pd.DataFrame(rows)
    st.write(pd.DataFrame(rows))
    # Print results.
    # for row in rows:
        # st.write(f"{row[0]} has a :{row[1]}:")

    # with my_cnx.cursor() as my_cur:
    #     my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")


# if st.button('From CSV'):
#     st.write("testing csv button..")
#     uploaded_file1 = st.file_uploader("Choose a file")

#     if uploaded_file1 is not None:
#         df = pd.read_csv(uploaded_file1)
#         st.write(df)
#     st.write("Testing completed!")

    
# Upload csv file, create dataframe 
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

    # Create Line & Bar chart from dataframe
    new_title3 = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">visualization</p>'
    st.markdown(new_title3, unsafe_allow_html=True)
    st.subheader('Click any button')
    tab1, tab2 = st.tabs(["Line Chart", "Bar Chart"])
    with tab1:
        st.header("Line chart visualization")
        st.line_chart(df, x='Name', y=['Percentage', 'Python_Marks', 'Azure_Marks', 'CSS_Marks'])
    with tab2:
        st.header("Bar chart Name vs Percentage")
        st.bar_chart(df, y=['Python_Marks', 'Azure_Marks', 'CSS_Marks'], x='Name')
else:
    st.info('☝️ Upload a CSV file')






