import streamlit as st
import segno
import time

st.set_page_config(
    page_title="QR CODES",
    page_icon="👾")

# add a banner
st.image("main_banner.png")

st.title("Welcome!")

# store user input
url = st.text_input("Please enter a URL")


def create_qrcode(url):
    qrcode = segno.make_qr(url)
    qrcode.to_pil(dark="lightblue", light = "white", scale = 5, border = 1).save("images/qrcode_streamlit.png")


if url:
    with st.spinner("generate QR Code"):
        time.sleep(1)
    create_qrcode(url)
    st.image("qrcode_streamlit.png",
             caption=("Here you go <3"),
             width = 300
    )

st.markdown(
    "<br><hr><center>Made with 🤍 by Svea",
    unsafe_allow_html=True)
