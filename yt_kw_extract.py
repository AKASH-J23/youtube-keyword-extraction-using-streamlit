import streamlit as st
from bs4 import BeautifulSoup
import requests

st.markdown("<h1 style='text-align: center;'> Youtube Keyword Extractor </h1>",unsafe_allow_html=True)
st.markdown("---",unsafe_allow_html=True)
url=st.text_input("Enter your URL")
btn=st.button("extract")
if btn:
    page=requests.get(url)
    soup=BeautifulSoup(page.content,"lxml")
    tag=soup.select("meta[name='keywords']")
    title=soup.find("title")
    keywords=tag[0].get("content")
    st.title("Title")
    st.markdown("<h6 style='color:#090d79 ;'>"+title.text+"</h6>",unsafe_allow_html=True)
    st.title("Keywords")
    st.markdown("<h6 style='color:#090d79 ;'>"+keywords+"</h6>",unsafe_allow_html=True)