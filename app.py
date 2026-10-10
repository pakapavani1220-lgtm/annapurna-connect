import streamlit as st

# 1. Set the page to wide mode to give your HTML more room
st.set_page_config(layout="wide", page_title="My Embedded HTML App")

# 2. Open and read the contents of your index.html file
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # 3. Render the HTML inside the Streamlit app
    # You can adjust the height (in pixels) to fit your content
    st.components.v1.html(html_content, height=900, scrolling=True)

except FileNotFoundError:
    st.error("Could not find index.html. Make sure it is in the same folder as app.py!")
