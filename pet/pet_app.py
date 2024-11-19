import streamlit as st
import requests

#set up page

st.set_page_config(
    page_title="pet app",
    page_icon="😻")

st.header("welcome to my pet app",
           divider="rainbow")

def get_cat_image():
    url = "https://cataas.com//cat"
    contents = requests.get(url)

    return contents.content

def get_dog_image_url():
    url = "https://random.dog/woof.json"
    contents = requests.get(url).json()
    dog_image_url = contents ['url']

    return dog_image_url


c1, c2 = st.columns(2)

with c1:
    cat_button = st.button("Click here for a cat image",
              help = "Click this button to see a cat image")
    if cat_button:
        cat_image = get_cat_image()
        st.image(cat_image, width=300, caption="my cat image :)")

with c2:
    dog_button = st.button("Click here for a dog image",
              help = "Click this button to see a dog image")
    if dog_button:
        dog_image_url = get_dog_image_url()

        while dog_image_url[:4] == ".mp4":
            dog_image_url = get_dog_image_url()

        st.image(dog_image_url, width=300, caption="my dog image :)")
