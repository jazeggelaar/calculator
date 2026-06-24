import streamlit as st #jesse-calculator.streamlit.app
page = 1
while True:
    if page == 1:
        st.title("calculator!")
        math = st.text_input("type here your math question")
        if st.button("run math"):
            answer = eval(math)
            st.write("calculated:", answer)
        if st.button("rules"):
            page = 2
    if page == 2:
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
            page = 3
        if st.button("i dont understand"):
            page = 5
        if st.button("ok"):
            page = 1
    if page == 3:
        st.write("[parent]:")
        st.write("| [string]")
        if st.button("extra information"):
            page = 4
        if st.button("back"):
            page = 2
    if page == 4:
        st.write(": as /")
        st.write("x as *")
        if st.button("back"):
            page = 3
    if page == 5:
        st.write("unsupported = not allowed")
        st.write("supported = allowed")
        if st.button("back"):
            page = 2