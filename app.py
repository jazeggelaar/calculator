import streamlit as st #jesse-calculator.streamlit.app
st.title("calculator!")
math = st.text_input("type here your math question")
if st.button("run math"):
    answer = eval(math)
    st.write("calculated:", answer)
if st.button("rules(click here before use)"):
    st.switch_page("pages/rules.py")