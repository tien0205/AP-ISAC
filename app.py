import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trạm ISAC 3D", layout="wide",
                   initial_sidebar_state="collapsed")

# Bỏ lề, ẩn header/footer, ép khung HTML cao bằng màn hình
st.markdown("""
<style>
#MainMenu, header, footer {visibility: hidden; height: 0;}
.block-container {padding: 0 !important; max-width: 100% !important;}
iframe {height: 100vh !important; width: 100% !important; border: 0;}
</style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=900, scrolling=False)
