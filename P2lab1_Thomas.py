"""
(block comments -- continue until the triple quotes end)
# Thomas Jonathan
# 15Sept2026
# P2LAB 1
# CTI110
# Get Radius, Calculate and display diameter, circumference, and area
"""
PI = 3.14159

# Input -- get radius
radius = float(input("What is the radus fo the circle? "))

# Calculation -- find diameter, circumference, and area
# diameter = 2*r, circumference = 2*pi*r, area = pi*r*r
diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius

# Output -- .1f, .2f, 3.f
print(f"The diameter is {diameter:.1f}")
print(f"The circumference is {circumference:.2f}")
print(f"The area is {area:.3f}")