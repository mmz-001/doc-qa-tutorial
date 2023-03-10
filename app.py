import streamlit as st
from utils import parse_pdf, embed_text, get_answer

st.header("Doc QA")
uploaded_file = st.file_uploader("Upload docs", type=["pdf"])

if uploaded_file is not None:
    index = embed_text(parse_pdf(uploaded_file))
    query = st.text_area("ask me all about the ESRS (EU Sustainability reporting")
    button = st.button("Submit")
    if button:
        st.write(get_answer(index, query))
