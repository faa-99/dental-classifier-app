import streamlit as st

st.title("Train Custom CNN Model")
st.markdown(
    """This page allows training a custom Convolutional Neural Network having VGG16 as the base model. 
You can tune the hyper-parameters and perform training
"""
)
st.image(
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
    help="""The number of epochs when training the model."""
)

batch_size = st.sidebar.number_input(
    "Batch Size",
    value=8,
    min_value=4,
    max_value=32,
    help="""Batch size when training the model."""
)

optimizer = st.sidebar.selectbox("Optimizer",
                                 ('Adam', 'Adadelta', 'AdaMax', 'RMSprop'),
                                 label_visibility="visible",
                                 help="""Optimization algorithm used when training"""
                                 )

learning_rate = st.sidebar.selectbox("Learning Rate",
                                     (0.00001, 0.0001, 0.001, 0.01, 0.1),
                                     label_visibility="visible",
                                     help="""Learning rate used when training"""
                                     )
train_button = st.sidebar.button(label="Train the model!")
