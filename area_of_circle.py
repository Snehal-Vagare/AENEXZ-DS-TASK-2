import math

def area_of_circle(radius):
    return math.pi * radius * radius

radius = float(input("Enter radius of circle: "))
print(f"Area of circle with {radius} is: {round(area_of_circle(radius), 2)}")
