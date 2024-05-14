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
