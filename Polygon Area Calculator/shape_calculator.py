class Rectangle:

    #constructor
    def __init__(self, width, height, rectangle="Rectangle"):
        self.rectangle = rectangle
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
        return self.width


    def set_height(self, height):
        self.height = height
        return self.height

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
            return "Too big for picture."
        else:
            return picture

    def get_amount_inside(self, rectangle):
        amount = 0
        #"//" = floor division
        amount = self.width // rectangle.width * self.height // rectangle.height
        return amount


        
class Square(Rectangle):
    def __init__(self, side, width=0, height=0, square="Square", rectangle="Rectangle"):
        self.side = side
        self.square = square
        super(Square, self).__init__(width, height, rectangle="Rectangle")
        self.width += side
        self.height += side


    def set_side(self, side):
        self.side = side
        return self.side

    def set_width(self, width):
        width = width
        self.side = width
        return width, self.side


    def set_height(self, height):
        height = height
        return height


     #Return string version of Object
    def __str__(self):
        return str(self.square) + "(side=" + str(self.side) + ")"

    def get_picture(self):
        pic_width = "*" * self.side + "\n"
        picture = pic_width * self.side
        return picture
        
        
