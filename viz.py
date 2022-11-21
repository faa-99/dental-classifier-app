import os

from matplotlib import pyplot as plt, image as mpimg
from matplotlib.image import imread

DIR = 'assets/dataset'


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
