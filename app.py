import streamlit as st 
from collections import Counter 
from sklearn.cluster import KMeans
import addons
import cv2

st.set_page_config("Color Palette Finder", "Assets/site logo.png")
st.header(
    """
    Color Palette Extractor using Clustering...
    """
)

st.text(
    """
    Libraries Used: Collections, Sklearn, Matplotlib, Numpy, Open-CV, Pillow, Webcolors, Scipy
    Made By: Priyanshu N Bairwa
    """
)

st.sidebar.title("Enter Your Attributes Here...")



uploaded_file = addons.uploading_image()
k_value = st.sidebar.slider("Enter number of clusters", min_value=5, max_value= 50, value= 25, step= 5)
value_choice = st.sidebar.radio("Type of represent the colors", ["Hex Values", "Color Name"])
button = st.sidebar.button("Find Color Palette", False)

if uploaded_file is None and button:
    st.sidebar.warning("Error! Please Upload the image properly...") 

try:
    if button:
        with st.spinner("Processing..."):
            raw_image = addons.config_image(uploaded_file)
            img = raw_image

            if raw_image.shape[:2] >= (900, 600):
                img = cv2.resize(raw_image, (900, 600), interpolation= cv2.INTER_AREA)
            else:
                img = cv2.resize(raw_image, (900, 600), interpolation= cv2.INTER_CUBIC)

            img = img.reshape(img.shape[0] * img.shape[1], 3)


            model = KMeans(n_clusters= k_value)
            color_labels = model.fit_predict(img)
            center_colors = model.cluster_centers_

            counts = Counter(color_labels)
            ordered_colors = [center_colors[i] for i in counts.keys()]
            hex_code, color_name = addons.rgb_to_hex_color(ordered_colors)
            
            st.image(raw_image)

            if value_choice == "Hex Values":
                fig1 = addons.draw_piechart(counts, hex_code, hex_code)
            
            if value_choice == "Color Name":
                fig1 = addons.draw_piechart(counts, color_name, hex_code)

            st.pyplot(fig1)
        st.balloons()
except:
    pass
