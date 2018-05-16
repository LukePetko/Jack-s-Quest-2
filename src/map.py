print(__name__)

import json

from src.platforms import *

class Map():
    def __init__(self, data_set):
        self.canvas = data_set["canvas"]

        self.level = data_set["level_id"][0]
        self.stage = data_set["level_id"][1]

        self.enemies = list()
        self.platforms = list()

        self.create_level()

    def create_level(self):
        with open("src/maps/level_1_01.json") as f:
            level_data = json.load(f)

        for data in level_data["platforms"]:
            self.platforms.append(Platform(data))

        # for i in self.platforms:
        #     i.image.show()


    def draw(self):
        pass

    def delete_level(self):
        self.canvas.delete("level")
