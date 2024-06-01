class Person:
    def __init__(self, name, surname, gender, age, ID):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.personalID = ID

    def check_retirement_age(self):
        if self.gender.lower() in ['male', 'man']:
            if self.age >= 65:
                return "You have reached the retirement age."
            else:
                return f"You have {65 - self.age} years remaining to retirement."
        elif self.gender.lower() == 'female':
            if self.age >= 60:
                return "You have reached the retirement age."
            else:
                return f"You have {60 - self.age} years remaining to retirement."
        else:
            return "Retirement age criteria not defined for this gender."

    def age_difference(self, other_person):
        diff = abs(self.age - other_person.age)
        return diff

    def years_to_retirement(self):
        if self.gender.lower() in ['male', 'man']:
            return max(0, 65 - self.age)
        elif self.gender.lower() == 'female':
            return max(0, 60 - self.age)
        else:
            return "Retirement age criteria not defined for this gender."

# Example usage:
person1 = Person("John", "Doe", "male", 68, "12345")
person2 = Person("Jane", "Smith", "female", 62, "67890")

print(person1.age_difference(person2))  # Output: 6 (|68 - 62|)
print(person1.years_to_retirement())    # Output: 0 (John has reached retirement age)
print(person2.years_to_retirement())    # Output: 0 (Jane has reached retirement age)
