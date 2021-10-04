class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width *  self.height

    def get_perimeter(self):
        return 2* self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
    
        if self.width > 50  or self.height > 50:
          print("Too big for picture.")
          return "Too big for picture."
        else:
          figure = (("*" * self.width) + "\n") * self.height
          print(figure)
          return(figure)
      
    def get_amount_inside(self, obj):
        self.object = obj
        w_t = int(self.width / self.object.width)
        h_t = int(self.height / self.object.height)
        return w_t * h_t
    
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width,self.height)
    
class Square(Rectangle):
    
    def __init__ (self,side):
        self.width = side
        self.height = side
    
    def set_side(self,side):
        self.width = side
        self.height = side
    
    def set_width(self,width):
        self.width = width
        self.height = width
        
    def set_height(self, height):
        self.width = height
        self.height = height
    
    def __str__(self):
        return "Square(side={})".format(self.width)

