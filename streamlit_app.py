import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first' : [1,2,3,4],
    'second' : [10,20,30,40]
})

st.write("Here's our fist attempt at using data to create a table:")
st.write(df)