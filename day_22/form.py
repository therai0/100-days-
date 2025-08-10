""" 
Let's explore the form in streamlit
"""

import streamlit as st 

st.header("Streamlit Basic Form")


# let's create the simple form with input field and button
with st.form(key='demo_form'):
    # this is the input field
    username = st.text_input("Username*")
    feedback = st.text_area("Feedback*")
    submit_btn = st.form_submit_button("Submit")

if submit_btn:
    if username and feedback:
        st.success(f"Thank you {username} for your kind feedback")
    else:
        st.error("Please enter the required field")













# Explore the different tyeps of input fields

st.header("Exploring all the input fields form")
with st.form('explore_all'):
    name = st.text_input("Enter your name ?")
    password = st.text_input("Enter password",type="password") 
    age = st.number_input("Enter your age ?",min_value=1,max_value=200,step=1)
    gender = st.selectbox("Gender",["Male","Female","Other"])
    # multiple seletction
    subject = st.multiselect('Subject',["Sciecne",'Math','Computer science','English','Social'])
    # input type range
    price = st.slider("Price",0,1000,5)
    dob = st.date_input("Enter your date of birth.")
    created_at = st.time_input("Enter the current time.")
    # file uploader
    file = st.file_uploader("Select file",type=["pdf","png","jpeg"]) 
    agree = st.checkbox("I agree all the terms and condiion.")
    submit_button = st.form_submit_button("Submit")


if submit_button:
    st.success("Everthing is fine")
