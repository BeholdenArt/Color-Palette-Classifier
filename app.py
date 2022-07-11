from configparser import Interpolation
from turtle import color
import streamlit as st 
from collections import Counter 
from sklearn.cluster import KMeans
import addons
import cv2
from sklearn import metrics 

st.set_page_config("Color Palette Finder", "Assets/site logo.png")
st.header(
    """
    Color Palette Extractor
    """
)

st.text(
    """
    Classify the most dominant colors from the image and get a nicely represented pie
    chart of each color's dominance along with either its name or hexadecimal values.
    """
)
st.write("Created By: Priyanshu N Bairwa ([_Github_](https://github.com/BeholdenArt))")

st.sidebar.title("Enter Your Attributes Here...")



uploaded_file = addons.uploading_image()
k_value = st.sidebar.slider("Palette Size", min_value=5, max_value= 50, value= 25, step= 5)
color_choice = st.sidebar.radio("Type of represent the colors", ["Hex Values", "Color Name"])
button = st.sidebar.button("Find Color Palette", False)

if uploaded_file is None and button:
    st.sidebar.warning("Error! Please Upload the image properly...") 

try:
    if button:
        with st.spinner("Processing..."):
            raw_image = addons.config_image(uploaded_file)
            img = raw_image
            img = cv2.resize(raw_image, (8, 8), interpolation= cv2.INTER_AREA)
            img = img.reshape(img.shape[0] * img.shape[1], 3)


            model = KMeans(n_clusters= k_value)
            color_labels = model.fit_predict(img)
            center_colors = model.cluster_centers_

            counts = Counter(color_labels)
            ordered_colors = [center_colors[i] for i in counts.keys()]
            hex_code, color_name = addons.rgb_to_hex_color(ordered_colors)
            
            st.image(raw_image)

            if color_choice == "Hex Values":
                fig1 = addons.draw_piechart(counts, hex_code, hex_code)
    
            if color_choice == "Color Name":
                fig1 = addons.draw_piechart(counts, color_name, hex_code)

            st.pyplot(fig1)
        st.balloons()
except:
    pass
