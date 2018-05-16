print(__name__)

from tkinter import *

from src.map import *

c = Canvas()

map_data_set = dict()
map_data_set["canvas"] = c
map_data_set["level_id"] = (1, 1)

map = Map(map_data_set)

# for platform in map.platforms:
#     platform.image.show()

c.mainloop()
