import streamlit as st
from PIL import Image
import pandas as pd

df = pd.read_csv("data.csv",sep=";")
st.set_page_config(layout="wide")
img = Image.open("images/photo.png")
width, height = img.size
cropped_img = img.crop((0, 500, width, height))
cropped_img.save('images/photo_cropped.png')

col1, col2 = st.columns(2)

with col1:
    st.image(cropped_img)

with col2:
    st.title("Shi Li")
    content = """
    Hey there! I’m Shi Li, a Computer Science student living in Germany. I love turning ideas into code — whether that’s a small web app, a chatbot with personality, or digging into data to find cool insights.
This website is kind of my playground: a place to share projects I’ve built while learning Python, Java, AI, and more. Each project represents something new I’ve discovered, and I’m always curious about what I can build next.
I’m currently on the lookout for a Working Student position where I can grow, learn from real-world challenges, and contribute with my coding skills. Thanks for stopping by — feel free to jump around and explore my projects!
"""
    st.info(content)

st.write("Below are all the apps that I built, if you are interested or have any comments/suggestions, feel free to use the contact me section!")

col3,empty_col,col4 = st.columns([2,0.5,2])
row_length = len(df)
half_length = int(row_length/2)
with col3:
    for index, row in df[:half_length].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[half_length:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")