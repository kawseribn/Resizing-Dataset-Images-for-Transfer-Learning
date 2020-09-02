import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def plot_example_images(plt,directory_of_image):
    img_size = 48
    plt.figure(0, figsize=(12,20))
    ctr = 0

    for expression in os.listdir(directory_of_image+""):
        for i in range(1,6):
            ctr += 1
            plt.subplot(7,5,ctr)
            img = load_img(directory_of_image+"" + expression + "/" +os.listdir(directory_of_image+"" + expression)[i], target_size=(img_size, img_size))
            plt.imshow(img, cmap="gray")

    plt.tight_layout()
    return plt
