courses_tuple = ("math", ("algebra", "Geometry"), "science")
print("Accesing element:",courses_tuple[0])
print("Accesing sub element:",courses_tuple[1][1])
new_courses = ("chemistry", "physics")
all_courses = courses_tuple + new_courses
print("After concatinating:", all_courses)