import streamlit as st
st.write("[parent]:")
st.write("| [string]")
if st.button("extra information"):
    st.switch_page("pages/information_extra.py")
if st.button("back"):
    st.switch_page("pages/rules.py")