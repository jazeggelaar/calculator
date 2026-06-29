import streamlit as st
st.write("[text parent]:")
st.write("| [text]")
if st.button("extra information"):
    st.switch_page("pages/information_extra.py")
if st.button("back"):
    st.switch_page("pages/rules.py")