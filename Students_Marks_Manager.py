student = {
    "Name": input("Enter Name: "),
    "Age": int(input("Enter Age: ")),
    "Course": input("Enter Course: ")
}

print(student)
print(student["Name"])
student["Course"] = "B.Sc Ai & ML"
student["Age"]=21
print(student)
choice = input("Do you want to update the course? (yes/no):")
if choice == "yes" :
  student["Course"] = input("Enter new Course:")
  print(student)
else:
  print("No change made") 
