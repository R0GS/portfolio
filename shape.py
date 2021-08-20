class Shape():
    def __init__(self, w, l, s1):
        self.width = w
        self.length = l
        self.s1 = s1

    def what_am_i():
        print('I am a shape')





class Rectangle(Shape):        
    def calculate_perimeter(self):
        return (2 * (self.length + self.width))
    
        
class Square(Shape):
    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size(self, new_size):
        self.s1 += new_size

rectangle = Rectangle()
square = Square()
shape = Shape()

rectangle.what_am_i()
square.what_am_i()
