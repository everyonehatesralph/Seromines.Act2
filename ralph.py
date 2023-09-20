name = input("Name: ")
id = input("ID: ")
coursec = input("Course & Section: ")
g1 = eval(input("First quarter grade: "))
g2 = eval(input("Second quarter grade: "))
g3 = eval(input("Third quarter grade: "))
g4 = eval(input("Fourth quarter grade: "))

grade =(g1 + g2 + g3 + g4) / 4
print("Name: ", name)
print("ID: ", id)
print("Course & Section: ", coursec)
print("First quarter grade: ", g1)
print("Second quarter grade: ", g2)
print("Third quarter grade: ", g3)
print("Fourth quarter grade: ", g4)

print("Your final grade is", grade)

