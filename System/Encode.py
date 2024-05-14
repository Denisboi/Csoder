from struct import Struct

from System.Reader import Reader

from PIL import Image, ImageDraw



from System.Logger import Console



# --------------------------

# OBJECTS

# --------------------------

class SpriteGlobals:
    def __init__(self):
        self.shape_count = 0
        self.total_animation = 0
        self.total_textures = 0
        self.text_field_count = 0
        self.matrix_count = 0
        self.color_transformation_count = 0
        self.export_count = 0
        self.names = []

class SheetData:
    def __init__(self):
        self.size = (0, 0)
class SpriteData:
    def __init__(self):
        self.id = 0
        self.regions = []
class Region:
    def __init__(self):
        self.sheet_id = 0
        self.num_points = 0
        self.rotation = 0
        self.mirroring = 0
        self.shape_points = []
        self.sheet_points = []
        self.top = -32767
        self.left = 32767
        self.bottom = 32767
        self.right = -32767
        self.size = (0, 0)
        self.zero_x = 0
        self.zero_y = 0
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
      
    @property

    def position(self):
        return self.x, self.y
      
    @position.setter

    def position(self, value):
        self.x = value[0]
        self.y = value[1]

# METHODS
def ceil(integer) -> int:
    return round(integer + 0.5)
  
def encode_sc(data, fileName):
  pass
