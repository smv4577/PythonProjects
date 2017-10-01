# Sydney Vernatter
# January 19, 2017

class Student:
    def __init__(self, first, last, gpa):
        self.firstName = first
        self.lastName = last
        self.gpa = gpa

    def __str__(self):
        return self.firstName + " " + self.lastName + "\tGPA: " + str(self.gpa)

    # def setName(self):
    #
    # def setGPA(self):
