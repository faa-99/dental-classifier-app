import pandas as pd
import requests
import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

from viz import plot_accuracy_and_loss, plot_categories


st.set_page_config(
    page_title="Dental Classifier App", initial_sidebar_state="collapsed"
)
tab_1, tab_2, tab_3 = st.tabs(["Overview", "Train", "Classify"])

with tab_1:
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

with tab_2:
    st.title("Train Custom CNN Model")
    st.markdown(
        """This page allows training a custom Convolutional Neural Network having VGG16 as the base model. 
    You can tune the hyper-parameters and perform training
    """
    )
    accuracy_plot = st.image(
        "assets/Accuracy-Loss-Plot.png",
        caption="Model Learning",
        use_column_width="auto",
        channels="RGB",
        output_format="PNG",
    )

    st.sidebar.title("Hyper Parameters")
    epochs = st.sidebar.number_input(
        "Epochs",
        value=50,
        min_value=1,
        max_value=70,
        help="""The number of epochs when training the model.""",
    )

    batch_size = st.sidebar.number_input(
        "Batch Size",
        value=8,
        min_value=4,
        max_value=32,
        help="""Batch size when training the model.""",
    )

    optimizer = st.sidebar.selectbox(
        "Optimizer",
        ("Adam", "Adadelta", "AdaMax", "RMSprop"),
        label_visibility="visible",
        help="""Optimization algorithm used when training""",
    )

    learning_rate = st.sidebar.selectbox(
        "Learning Rate",
        (0.00001, 0.0001, 0.001, 0.01, 0.1),
        label_visibility="visible",
        help="""Learning rate used when training""",
    )
    if st.sidebar.button(label="Train the model!"):
        hyper_params = {
            "EPOCHS": epochs,
            "LEARNING_RATE": learning_rate,
            "OPTIMIZER": optimizer
        }
        print(f"Body of request\n{hyper_params}")
        res = requests.post(
            "http://127.0.0.1:8000/api/DentalClassifier/TrainCustomVGG16",
            json=hyper_params,
        )
        acc_loss_plot = plot_accuracy_and_loss(res)
        st.pyplot(acc_loss_plot)

with tab_3:
    st.title("Classify XRay Image")
    st.markdown(
        """This page allows classifying a dental X-Ray image into one of the categories that the model was trained on
    """
    )
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded user image")

    if st.button("Classify") and uploaded_file is not None:
        files = {"image": uploaded_file.getvalue()}
        res = requests.post(
            "http://127.0.0.1:8000/api/DentalClassifier/ClassifyImage", files=files
        )
        st.write(res.json())
