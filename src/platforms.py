print(__name__)

from PIL import Image

platform_img_1 = Image.open("src/images/bg.png")

class Platform:
    def __init__(self, data_set):
        self.coords = (data_set[0 : 4])

        self.crop_image()


    def crop_image(self):
        self.image = platform_img_1.crop(self.coords)

        print("orezavam")
