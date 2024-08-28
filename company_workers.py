import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("The Best Company")
content = """Consider these descriptive words: Authentic: A company that stays true
 to its values and promises. Innovative: A company that is known for pushing
  boundaries and introducing new ideas. Trustworthy: A company that is reliable
   and fosters trust with its customers. Memorable: A company that leaves a lasting
    impression on its customers."""
st.info(content)
st.subheader("Our Team")
col1,col2,col3 = st.columns(3)
df = pandas.read_csv("workers_data.csv",sep=",")
with col1:
    for index,row in df[:4].iterrows():
        st.subheader(row["first name"].capitalize() +" "+ row["last name"].capitalize())
        st.write(row["role"])
        st.image("workers_images/" + row["image"])

with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(row["first name"].capitalize() +" "+ row["last name"].capitalize())
        st.write(row["role"])
        st.image("workers_images/"+ row["image"])

with col3:
    for index,row in df[8:].iterrows():
        st.subheader(row["first name"].capitalize() + " "+ row["last name"].capitalize())
        st.write(row["role"])
        st.image("workers_images/"+ row["image"])





















