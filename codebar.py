from unicodedata import name


class Member:
    def __init__ (self, full_name):
        self.full_name = full_name

    def introduce(self):
        print(f"Hello, my name is {self.full_name}!")

class Student(Member):
    def __init__ (self, full_name, reason):
        super(). __init__ (full_name)
        self.reason = reason

class Instructor(Member):
    def __init__ (self, full_name, bio, skills, add_skill):
        super(). __init__ (full_name)
        self.bio = bio
        self.skills = skills
        self.add_skill = add_skill

class Workshop:
    def __init__ (self, date, subject, instructors, students):
        self.date = date
        self.subject = subject
        self.instructors = instructors = []
        self.students = students = []
    
    def add_participant (self, member):
        if type(name) is Student:
            self.students.append(name)
        else:
            self.instructors.append(name)

    def print_details(self):
        print(f"Workshop - {self.date} - {self.subject}")
        print("Students")
        for idx
    # def add_participant (self, member):
    #     self.member = member
    #     if (type(member).__name__) == 'Student':
    #         self.students.append(member)
    #     elif (type(member).__name__) == 'Instructor':
    #         self.instructors.append(member)
    #     else:
    #         print ("unknown member")

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
   
    # def add_participant (self, member):
    #     if type(name) is Student:
    #         self.students.append(name)
    #     else:
    #         self.instructors.append(name)

    # def print_details(self):
    #     print(f"Workshop - {self.date} - {self.subject}")
    #     print("Students")
    #     for idx