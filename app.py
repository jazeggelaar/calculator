import streamlit as st #jesse-calculator.streamlit.app
rules_visibility = True
st.title("calculator!")
math = st.text_input("type here your math question")
if st.button("run math"):
    answer = eval(math)
    st.write("calculated:", answer)
    rules_visibility = False
if rules_visibility:
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