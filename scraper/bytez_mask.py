import io
import requests
from PIL import Image
import numpy as np
from bytez import Bytez

class BytezMaskGenerator:
    def __init__(self, bytez_key):
        self.sdk = Bytez(bytez_key)
        self.model = self.sdk.model("dreamlike-art/dreamlike-photoreal-2.0")
        self.model.create()

    def generate_mask(self, symbol, width=800, height=400):
        prompt = f"""
        A flat, solid black silhouette of a fully black{symbol}, centered, on a pure white background(Including floor). The background having strictly no gray.
        The background is white as milk.
        Only two colors: pure black (#000000) and pure white (#FFFFFF).
        Minimalistic and high contrast.
        """
        output, error = self.model.run(prompt)
        if error:
            print("Bytez error:", error)
            return None

        if isinstance(output, str) and output.startswith("http"):
            img_bytes = requests.get(output).content
            img = Image.open(io.BytesIO(img_bytes)).convert("L")
            img = img.resize((width, height), Image.LANCZOS)
            return img
        else:
            print("Unexpected Bytez output format:", output)
            return None

def create_circle_mask(width, height, margin=20):
    mask = np.ones((height, width), dtype=np.uint8) * 255
    cx, cy = width // 2, height // 2
    r = min(cx, cy) - margin
    y, x = np.ogrid[:height, :width]
    circle = (x - cx) ** 2 + (y - cy) ** 2 <= r * r
    mask[circle] = 0
    return mask