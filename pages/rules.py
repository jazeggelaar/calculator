import streamlit as st
st.write("rules:")
st.write("| unsupported:")
st.write("| | letters")
st.write("| | symbols")
st.write("| supported:")
st.write("| | /")
st.write("| | *")
st.write("| | -")
st.write("| | +")
st.write("| | nummbers")
if st.button("information about rules"):
    page_wanted = 3
if st.button("i dont understand"):
    st.switch_page("pages/5.py")
if st.button("ok"):
    st.switch_page("pages/app.py")