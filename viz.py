import os

from matplotlib import image as mpimg
from matplotlib import pyplot as plt
from matplotlib.image import imread


DIR = "assets/dataset"


def plot_categories():
    images = os.listdir(DIR)
    data_path = [os.path.join(DIR + "/" + i) for i in images]
    fig = plt.figure(figsize=(10, 10))
    for i, file in enumerate(data_path):
        plt.subplot(3, 2, i + 1)
        plt.imshow(imread(file))
        plt.title(os.path.basename(file))
        plt.axis("off")
    return fig


def plot_accuracy_and_loss(history):
    acc = history["accuracy"]
    val_acc = history["val_accuracy"]

    loss = history["loss"]
    val_loss = history["val_loss"]

    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(acc, label="Training Accuracy")
    plt.plot(val_acc, label="Validation Accuracy")
    plt.legend(loc="lower right")
    plt.ylabel("Accuracy")
    plt.ylim([min(plt.ylim()), 1])
    plt.title("Training and Validation Accuracy")

    plt.subplot(2, 1, 2)
    plt.plot(loss, label="Training Loss")
    plt.plot(val_loss, label="Validation Loss")
    plt.legend(loc="upper right")
    plt.ylabel("Cross Entropy")
    plt.title("Training and Validation Loss")
    plt.xlabel("epoch")

    return plt.gcf()
