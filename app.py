import streamlit as st #jesse-calculator.streamlit.app
st.title("calculator!")
math = st.text_input("type here your math question")
if st.button("run math"):
    if type(math) == ("string"):
        answer = eval(math)
        st.write("calculated:", answer)
    else:
        st.write("check the rules again")
if st.button("rules(click here before use)"):
    st.switch_page("pages/rules.py")