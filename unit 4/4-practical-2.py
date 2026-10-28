def show_student(name, course):
    print(name, "studies", course)


def welcome(name="Student"):
    print("Welcome,", name)


def show_values(*args):
    print("Values:", args)


def show_details(**kwargs):
    print("Details:", kwargs)


show_student("Piyush", "Python")
show_student(course="Python", name="Piyush")

welcome()
welcome("Piyush")

show_values(10, 20, 30)
show_details(name="Piyush", course="Python")
