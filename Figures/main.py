import classes

c1 = classes.Circle(2, 4, 4)
t1 = classes.Triangle(1, 20, 3, 43, 5, 1)
sq1 = classes.Square(1, 5, 2, 9)

print(f"Периметр круга равен {round(c1.circle_perimeter(), 2)}, площадь равна {round(c1.circle_perimeter(), 2)}")
print(f"Периметр треугольника равен {round(t1.triangle_area(), 2)}, площадь = {round(t1.tr_per(), 2)}")
print(f"Периметр квадрата равен {round(sq1.square_area(), 2)} площадь равна {round(sq1.square_perimeter(), 2)}")
