import re
import numpy as np

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def pil_to_wordcloud_mask(pil_img):
    arr = np.array(pil_img)
    mask = np.where(arr > 128, 255, 0).astype(np.uint8)
    return mask