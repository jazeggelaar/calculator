import streamlit as st #streamlit run app.py
st.title("calculator!")
math = st.text_input("type here your math question")
if st.button("run math"):
    answer = eval(math)
    st.write("calculated:", answer)