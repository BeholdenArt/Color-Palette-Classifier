import numpy as np
from matplotlib import pyplot as plt
from webcolors import CSS3_HEX_TO_NAMES, hex_to_rgb
from scipy.spatial import KDTree
from PIL import Image
import streamlit as st


def uploading_image():
    uploaded_file = st.sidebar.file_uploader("Upload Your Image", type=["png", "jpg", "jpeg"])
    return uploaded_file


def rgb_to_hex_color(rgb_list):
    hex_list = []
    color_list = []
    for rgb_tuple in rgb_list:
        css3_db = CSS3_HEX_TO_NAMES
        names = []
        rgb_values = []
        hex_value = []
        
        for color_hex, color_name in css3_db.items():
            names.append(color_name)
            rgb_values.append(hex_to_rgb(color_hex))
            hex_value.append(color_hex)

        kdt_db = KDTree(rgb_values)
        distance, index = kdt_db.query(rgb_tuple)
        
        hex_list.append(hex_value[index])
        color_list.append(names[index])

    return hex_list, color_list


def config_image(image_file):
    img = Image.open(image_file)            # Streamlit Upload Type -> PIL Image Type
    np_img = np.array(img)                  # PIL Image Type -> Numpy Array
    return np_img


def draw_piechart(counts, choice, hex_code): 
    fig1, ax1 = plt.subplots()
    ax1.pie(counts.values(), labels=choice, colors=hex_code)
    ax1.axis('equal') 
    return fig1
