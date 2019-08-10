class RadiusArea():
    def __init__(self,r):
        self.radius = r
    def radiue(self):
        return self.radius **2*3.14
    def perimeter(self):
        return 2 * self.radius * 3.14
NewRadius = RadiusArea(8)
print(NewRadius.radiue)
print(NewRadius.perimeter())
