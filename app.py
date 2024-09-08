import streamlit as st
import os
import sqlite3
import google.generativeai as genai
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure google api key
genai.configure(api_key='AIzaSyAj74_vKePZ4pSDbDCtOUp88m2AoGJedUE')

# Function to load google gemini model and provide sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the sql database
def ready_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

prompt =[ """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION and MARKS \n\nFor example, \nExample 1- How many entries of records are present?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
\nExample 2- Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * FROM STUDENT where CLASS = 'Data Science';
also the sql code should not have ``` in beginning or end and sql word in the output 
"""
]

st.set_page_config(page_title = 'I can Retrieve Any SQL query')
st.header("SQL LLM")
question = st.text_input("Input: ", key = 'input')
submit = st.button('Ask the question')

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    data = ready_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in data:
        length = len(row)
        st.text('\t\t'.join([str(row[i]) for i in range(length)]))