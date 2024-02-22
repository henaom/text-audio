import sreamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image 

st.title ("Interfaces Multimodales")
image = Image.open("imagenh.jpeg")

st.image(image, width=200)
