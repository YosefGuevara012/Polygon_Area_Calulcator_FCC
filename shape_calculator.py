class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self,width):
    self.width = width

  def set_height(self, height):
    self.height(height)

  def get_area(self):
    return self.width *  self.height

  def get_perimeter(self):
    return 2* self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    
    if self.width > 50  or self.height > 50:
      print("Too big for picture.")
    else:
      for i in range(self.height):
        print("*" * self.width) 



class Square(Rectangle):

  def set_side(self,side):
    self.width = side
    self.height = self.height
