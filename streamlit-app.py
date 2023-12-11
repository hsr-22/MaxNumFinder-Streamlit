import streamlit as st
import base64

st.set_page_config(
    page_title="MaxNumFinder",
    page_icon=":notebook_with_decorative_cover:",
    # layout="wide"
)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('app-bkg.png')

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

st.title('The Largest Among Us')

num1 = st.number_input('Enter your first', value=0)
num2 = st.number_input('Enter your second', value=0)
num3 = st.number_input('Enter your third', value=0)

if st.button('Find the Largest'):
    result = find_largest(num1, num2, num3)
    st.markdown('<span style="color:blue;">The largest one is <b>{result}</b></span>', unsafe_allow_html=True)
    # st.write(f'The largest one is {result}')
    # st.markdown(f'<p style="color:blue;">The largest one is **{result}**</p>', unsafe_allow_html=True)
