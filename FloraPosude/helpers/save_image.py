import secrets, os
from PIL import Image

from FloraPosude import basedir


def save_image(image):
    random_hex = secrets.token_hex(8)
    _, ext = os.path.splitext(image.filename)
    picture_filename = random_hex + ext
    picture_path = os.path.join(basedir, "static/images/plants", picture_filename)
    picture_size = (300, 210)
    i = Image.open(image)
    i.thumbnail(picture_size)
    i.save(picture_path)
    return picture_filename
