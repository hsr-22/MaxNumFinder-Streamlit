import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

st.title('The Largest Among Us')

num1 = st.number_input('Enter your first', value=0)
num2 = st.number_input('Enter your second', value=0)
num3 = st.number_input('Enter your third', value=0)

if st.button('Find the Largest'):
    result = find_largest(num1, num2, num3)
    st.write(f'The largest one is {result}')
