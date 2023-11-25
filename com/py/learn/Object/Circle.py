import matplotlib.pyplot as plt

class Circle(object):
    # Class attributes (shared by all instances)
    class_attribute = 100

    # Constructor method (initialize instance attributes)

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def add_radius(self, radius):
        self.radius = self.radius * radius
        return self.radius

    def draw(self):
        print(f"Constructing a circle with radius {self.radius} and color {self.color}")
        # plt.gca().add_patch(plt.Circle((0, 0), self.radius, fc=self.color))
        # plt.axis('scaled')
        # plt.show()


c1 = Circle(radius=1, color='Red')
c1.draw()
c1.add_radius(100)
c1.draw()
c1.add_radius(2)
c1.draw()

blueCircle = Circle(10, 'blue')
blueCircle.draw()
print(blueCircle.color)
print(dir(blueCircle))
blueCircle.__setattr__("radius", 27)
blueCircle.draw()
print(blueCircle.__getattribute__("color"))
print(blueCircle.__str__())

# empty = Circle()
# print(empty.color)


print("****************Class Attribute Vs Instance Variable")
#If class attr value is modified using instance , then only for that instance the value will change
print(Circle.class_attribute)
c1.class_attribute = 200
print(Circle.class_attribute, c1.class_attribute)
print(Circle.class_attribute, blueCircle.class_attribute)

Circle.class_attribute = 500
print("***")
print(Circle.class_attribute, c1.class_attribute)
print(Circle.class_attribute, blueCircle.class_attribute)
