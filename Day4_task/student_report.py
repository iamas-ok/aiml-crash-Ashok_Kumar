# Task 01: Class-Based Student Report
# Creates a Student class with grade logic and prints formatted report cards.

class Student:
    # EXPLORE- class variable shared by all instances
    school_name = "CodeTrade"  

    def __init__(self, name: str, roll_no: int, marks: list[float]):
        # Instance variables 
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self) -> float:
        # Returns the average of the student's marks
        return sum(self.marks) / len(self.marks)

    def grade(self) -> str:
        # Returns a letter grade based on the average marks
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 45:
            return 'D'
        else:
            return 'F'

    def __str__(self) -> str:
        # Returns a formatted string representation of the student's report card
        return (
            f"[{Student.school_name}] | Roll No: {self.roll_no:03d} | "
            f"Name: {self.name} | Avg: {self.average():.1f} | Grade: {self.grade()}"
        )



s1 = Student("Aarav", 1, [92, 88, 95])
s2 = Student("Priya", 2, [74, 68, 80])
s3 = Student("Rohan", 3, [40, 55, 38])

for student in [s1, s2, s3]:
    print(student)

# EXPLORE note-->
# Instance variables (self.name, self.roll_no, self.marks) are unique per object.
# Class variable (school_name) is shared across ALL Student instances.
# Changing Student.school_name updates it for every object at once.