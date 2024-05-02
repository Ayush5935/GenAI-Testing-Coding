import streamlit as st

def generate_python_code(string_to_print):
    code = f"print('{string_to_print}')"
    return code

st.title("Python Code Generator")

string_to_print = st.text_input("Enter the string to print:")
if st.button("Generate Code"):
    generated_code = generate_python_code(string_to_print)
    st.code(generated_code, language="python")
