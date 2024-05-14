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
