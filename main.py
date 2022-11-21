import pandas as pd
import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

from viz import plot_categories

st.set_page_config(
    page_title="Dental Classifier App", page_icon="🦷", initial_sidebar_state="collapsed"
)

st.title("🦷 Dental Classifier")
st.markdown(
    """The purpose of this project is to classify dental X-Ray images into 5 classes by proposing a deep learning model. 
The pre-trained VGG16 model was used as a base model, followed by a convolutional neural network model. The 
architecture is depicted in the figure below. Training was done using dental x-rays from the UFBA_UESC
dental images dataset which includes structural variations regarding the number of teeth,
restorations, implants, appliances, and the size of the mouth and jaws."""
)

st.image(
    "assets/arch.png",
    caption="Model Architecture",
    use_column_width="auto",
    channels="RGB",
    output_format="PNG",
)

st.subheader("Dataset")
d = {
    "Number": [1, 2, 4, 6, 10],
    "Category": [
        "Images with all the teeth, containing teeth with restoration and with "
        "dental appliance",
        "Images with all the teeth, containing teeth with restoration and "
        "without dental appliance",
        "Images with all the teeth, containing teeth without restoration and "
        "without dental appliance",
        "Images containing more than 32 teeth",
        "Images missing teeth, containing teeth without restoration and without "
        "dental appliance",
    ],
}
df = pd.DataFrame(data=d)
# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(df)

dataset_dist = (
    Bar()
    .add_xaxis(["cat1", "cat2", "cat4", "cat6", "cat10"])
    .add_yaxis("Images", [73, 220, 140, 170, 115])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Number of images in each category")
    )
)
st_pyecharts(dataset_dist)

st.subheader("Image Preview")
fig = plot_categories()
st.pyplot(fig)

st.subheader("References")
st.markdown(
    """Gil Silva, Luciano Oliveira, Matheus Pithon, Automatic segmenting teeth in
    X-ray images: Trends, a novel data set, benchmarking and future perspectives, Expert Systems With
    Applications (2018), doi: 10.1016/j.eswa.2018.04.001"""
)
