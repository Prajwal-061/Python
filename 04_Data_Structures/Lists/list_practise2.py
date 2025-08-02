places=['pokhara','lumbini','chitwan','mustang']
print("\nraw list of the places:",places)

print("the sorted list",sorted(places))
print("\nthe original order of the list is:",places)

print("the reversed sorted list is:",sorted(places,reverse=True))
print("\nthe original list remains unchanged",places)

print("\n using reverse to change the order of the list:")
places.reverse()
print(places)
places.reverse()
print("\nthe original order remains unchanged",places)

print("\nusing sort method to arrange in alphabetical order")
places.sort()
print(places)
print("\nthe original order of the list has been changed now:",places)

places.sort(reverse=True)
print(places)

print("\nthe original order has been changed again",places)

