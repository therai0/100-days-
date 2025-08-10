import streamlit as st 
import pandas as pd
import numpy as np


# working with simple pandas dataframe 
st.header("Learn Streamlit with Pandas and numpy")
dit = {
    "Richest person":["Bhaskar Rai","Bishal Kafle","Ayush Dahal","Jemish Chudal"],
    "Networth(US$)":["10.5B","9.1B","2.5B","1B"],
    "Company":["BnB tech","Xyz Inc","Dahal Group","Jems Group"],
}
# creating the dataframe 
df = pd.DataFrame(dit)
st.write(df)



# read the  csv file and print the data 
st.header("Read the CSV file")
read_data = pd.read_csv('costumer.csv')
st.write(read_data)

# developing the line chart in streamlit
st.subheader("Line char with streamlit and pandas")
chart_data = pd.DataFrame(
    np.random.randn(20),
    columns=['a']
)
# this helps to build the line chart
st.line_chart(chart_data)

# area chart
st.subheader("Area chart")
st.area_chart(chart_data)

# bar chart
st.subheader("Bar chart")
st.bar_chart(chart_data)


