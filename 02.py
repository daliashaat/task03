
def triangle_area():
    base = int(input("Enter Base: "))
    height = int(input("Enter height"))

    return 0.5 * base * height

print(triangle_area())
average = triangle_area()
if average >= 10:
    print("large")
elif average < 10:
    print("small")
if average <= 0:
    print("invalid")

def triangle_perimeter():
    side1 = int(input("Enter side1"))
    side2 = int(input("Enter side2"))
    side3 = int(input("Enter side3"))
    return side1 + side2 + side3
print(triangle_perimeter())
def square_area():
    side = int(input("Enter side"))
    return side * 4
print(square_area())
average = square_area()
if average >= 10:
    print("large")
elif average < 10:
    print("small")
if average <= 0:
    print("invalid")

def square_perimeter():
    side = int(input("Enter side"))
    return 4 * side
print(square_perimeter())
def circle_area():
    side = int(input("Enter side"))
    return side*side*3.14
print(circle_area())
average = circle_area()
if average >= 10:
    print("large")
elif average < 10:
    print("small")
if average <= 0:
    print("invalid")


