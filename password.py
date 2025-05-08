import random
import string
import streamlit as st

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected!")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit app
st.title("🔐 Password Generator")

length = st.number_input("Password length", min_value=4, max_value=100, value=12)
use_upper = st.checkbox("Include uppercase letters", value=True)
use_digits = st.checkbox("Include digits", value=True)
use_symbols = st.checkbox("Include symbols", value=True)

if st.button("Generate Password"):
    try:
        password = generate_password(length, use_upper, use_digits, use_symbols)
        st.success(f"Generated Password: `{password}`")
    except ValueError as e:
        st.error(str(e))
