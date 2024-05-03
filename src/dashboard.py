import streamlit as st 
from src.password_generators import PinCodeGenerator, RandomPasswordGenerator, MemorablePasswordGenerator


st.image("stereamlit-password-generator/images/password-image.jpeg", width=400)
st.title(":zap: Password generator")

option = st.radio(
    'Select a Password generator',
    ("Random Password", 'Pin Code', 'Memorable Password')
)

if option == 'Pin Code':
    length = st.slider("Select the length of the pin code", 4, 32)
    generator = PinCodeGenerator(length)
elif option == 'Random Password':
    include_capitalization = st.toggle("Include capitals")
    include_numbers = st.toggle("Include numbers")
    include_symbols = st.toggle("Include symbols")
    length = st.slider("Select the length of the password", 8, 100)
    generator = RandomPasswordGenerator(include_capitalization, include_numbers, include_symbols, length)
elif option == 'Memorable Password':
    no_of_words = st.slider("Select the number of words in the password", 2, 10)
    separator = st.text_input("Enter a separator for the words in the password:")
    capitalization = st.checkbox("Capitalize the words in the password")
    generator = MemorablePasswordGenerator(no_of_words, separator, capitalization)

password = generator.generate()
st.write(f"Your password is: ```{password}```")


