set1 = {1,2,3,4,5}
set2 = {2,4,6,8,10}

set_union = set1.union(set2)
print("union is:", set_union )

set_intersection = set1.intersection(set2)
print("Intersection is:", set_intersection)

set_difference = set1.difference(set2)
print("Difference is:", set_difference)

set1.add(6)
print("After adding new element:" ,set1)
set2.add(12)
print("After adding new element:", set2)