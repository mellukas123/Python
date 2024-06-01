#Create a class called "Person" with attributes for name and age.
#Add a method to the Person class that prints a greeting message with the person's name.
#Create a subclass of Person called "Student" with an additional attribute for student ID.
#Override the Person class's method in the Student subclass to include the student ID in the greeting message.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello and welocome, dear ", self.name)

class Student(Person): #Student should inherit from Person
    def __init__(self, name, age, student_ID):
        super().__init__(name, age)
        self.student_ID = student_ID

    def greeting(self):
        print("Hello and welcome, dear ", self.name + ",", "Your student ID is", self.student_ID)

person1 = Person("Alice", 25)
person1.greeting()

student1 = Student("Bob", 20, "12345")
student1.greeting()