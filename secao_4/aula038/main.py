# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from pathlib import Path
from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'wallhaven.png'
NEW_IMAGE = ROOT_FOLDER / 'new_image.png'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size

new_width = 653
new_height = round(height * new_width / width)

new_image = pil_image.resize((new_width, new_height))
new_image.save(

    NEW_IMAGE,
    optimize=True,
    quality=100

)
