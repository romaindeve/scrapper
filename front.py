import streamlit as st
import pandas as pd
import numpy as np
from newspaper import Article

default_text = "Paste the url of the website you want to scrap"


st.title('Online scrapper')

st.session_state['url'] = st.text_area(
        "Entrez un extrait d'article de journal", value=default_text)

if st.session_state['url'] != default_text and len(st.session_state['url']) > 0 :
    article = Article(st.session_state['url'])
    article.download()
    article.parse()
    st.write(f"## {article.title}")
    st.write(f"_{article.author}_")
    st.write(f"{article.text}")