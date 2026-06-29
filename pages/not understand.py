import streamlit as st
st.write("unsupported = not allowed")
st.write("supported = allowed")
if st.button("back"):
    st.switch_page("pages/rules.py")