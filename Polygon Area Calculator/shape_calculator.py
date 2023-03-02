class Rectangle:

    #constructor
    def __init__(self, width, height, rectangle="Rectangle"):
        self.rectangle = rectangle
        self.width = width
        self.height = height

    def set_width(self, width):
        width = width
        return width


    def set_height(self, height):
        height = height
        return height

    def get_area (self):
        area = self.width * self.height
        return area

    def get_perimeter (self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal (self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    #Return string version of Object
    def __str__(self):
        return str(self.rectangle) + "(width=" + str(self.width) + "," + " height=" + str(self.height) + ")"
    
    def get_picture(self):
        pic_width = "*" * self.width + "\n"
        picture = pic_width * self.height
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        else:
            return picture
        
class Square(Rectangle):
    def __init__(self, side, width=0, height=0, square="Square", rectangle="Rectangle"):
        self.side = side
        self.square = square
        super(Square, self).__init__(width, height, rectangle="Rectangle")
        self.width += side
        self.height += side


    def set_side(self, side):
        side = side
        return side

    def set_width(self, width):
        width = width
        return width


    def set_height(self, height):
        height = height
        return height


     #Return string version of Object
    def __str__(self):
        return str(self.square) + "(side=" + str(self.side) + ")"
        
        
