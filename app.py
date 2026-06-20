import streamlit as st
st.title("calculator!")
math = st.text_input("type here your math question")
if st.button("run math"):
    answer = eval(math)
    st.write("calculated:", answer)