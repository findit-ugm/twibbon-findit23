import cv2
import os
import requests
import instaloader
import numpy as np

current_dir = os.path.join(os.getcwd(), "src", "tmp")


def download_img(ig_url):
    os.chdir(current_dir)
    if ig_url[-1] == '/':
        ig_url = ig_url[:-1]
    url = ig_url[-11:]
    L = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(L.context, url)
    L.download_post(post, target=f"{url}")
    return url

def load_image(img_url):
    url = download_img(img_url)
    file_list = os.listdir(os.path.join(current_dir, url))
    for filename in file_list:
        _path = os.path.join(url, filename)
        path = os.path.join(current_dir, _path)
        if ("jpg" or "jpeg" or "png" or "webp") in filename:
            img = cv2.imread(path)
            image = cv2.resize(img, dsize=(224,224), interpolation=cv2.INTER_AREA)
        else:
            os.remove(path)
    return np.expand_dims(image, axis=0)