class Rectangle:

  def __init__(self, width=0.0, height=0.0):
    self.width = width 
    self.height = height

  def __str__(self):
    return "Rectangle(width={0}, height={1})".format(self.width, self.height)

  # Set the instance's width if not initially done when constructed
  def set_width(self, width):
    self.width = width

  # Set the instance's height if not initially done when constructed
  def set_height(self, height):
    self.height = height

  # Get the Area of the instance
  def get_area(self):
    return self.width * self.height

  # Get the Perimeter of the instance
  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  # Get the Diagonal of the instance 
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)

  # Construct a picture of the instance using asterisks `*`
  def get_picture(self):
    # Test if height or width is greater than 50
    if (self.height > 50 or self.width > 50):
      return "Too big for picture."

    picture = ''
    for x in range(self.height):
      picture += ('*' * self.width)
      picture += '\n'

    return picture

  def get_amount_inside(self, shape):
    area_shape = shape.get_area()
    counter = 0
    area_self = self.get_area()
    while area_self >= area_shape:
      area_self -= area_shape
      counter += 1

    return counter


class Square(Rectangle):

  def __init__(self, side=0):
    super().__init__(side, side) 

  def __str__(self):
    return "Square(side={0})".format(self.width)

  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)


  