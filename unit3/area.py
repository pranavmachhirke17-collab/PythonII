import shape

print("choice")
print("n1: Area of circle")
print("n2: Area of Rectangle")
print("n3: Area of triangle")

choice = int(input("Enter your choice: "))
if choice == 1:
    radius = float(input("Enter the radius:"))
    area1 = shape.area_circle(radius)
    print("Area of circle is:", area1)

if choice == 2:
    length = float(input("Enter length:"))
    width = float(input("Enter breadth:"))
    area2 = shape.area_rectangle(length, width)
    print("Are of rectangle is:", area2)

if choice == 3:
    base = float(input("Enter base:"))
    height = float(input("Enter height:"))
    area3 = shape.area_triangle(base,height)
    print("Area of triangle is:", area3)
