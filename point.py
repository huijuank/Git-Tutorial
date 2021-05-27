import matplotlib.pyplot as plt

class Point:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def show(self):
        print(f'X,Y,Z coordinates are ({self.x},{self.y},{self.z}).')
        ax = plt.axes(projection='3d')
        ax.scatter(self.x,self.y,self.z)
        ax.set(xlabel='X axis', ylabel='Y axis', zlabel='Z axis')
        plt.show()
        
    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz
        
    def dist(self, other):
        distance = ((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)**0.5
        print(f'Distance between 2 points is {distance}')
        
p1 = Point(1,5,2)
p1.show()
p1.move(2,-1,-2)
p1.show()
p2 = Point(1,5,2)
p2.show()
p1.dist(p2)