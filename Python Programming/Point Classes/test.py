from point import Point, DimensionalPoint

# p1 = Point((1, 2))
# print(p1)

# p2 = Point((0, 1.5))
# print(p1 == p2)

# p3 = Point((1, 0.5))
# p4 = p2 + p3
# print(p4)

# print(p1 == p4)

# # print(p2)
# p2.add(p3)
# # print(p2)
# # print(p2)
# # print(p1)
# # print(p2)
# # print(p2)
# print(p1 == p2)

# p1.distance_to(p3)


p1 = DimensionalPoint((1,2,3))
print(p1)
p2 = DimensionalPoint((2,5,7))
print(p1 == p2)
p1.add(p2)
p3 = DimensionalPoint((3,7,10))
print(p1 == p3)
p4 = p1 + p3
print(p4.distance_to(p2))
p5 = DimensionalPoint((5, 4.5, 3, 2.5, 1, 0.5, -1))
print(p5)
