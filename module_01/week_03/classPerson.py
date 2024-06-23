
class Ward:
    def __init__(self, ward_name):
        self.__wardname = ward_name
        self.__lst_person = []

    def get_wardname(self):
        return self.__wardname

    def add_person(self, person):
        self.__lst_person.append(person)

    def get_lst_person(self):
        return self.__lst_person

    def sort_age(self):
        self.__lst_person.sort(
            key=lambda person: person.get_yob(), reverse=True)

    def describe(self):
        print(self.get_wardname())
        for person in self.get_lst_person():
            description = person.describe()
            print(description)

    def count_doctor(self):
        count = 0
        for person in self.get_lst_person():
            if isinstance(person, Doctor):
                count += 1
        print(f"The Number of Doctors in this Ward is {count}")
        return count

    def compute_average(self):
        lst = []
        for person in self.get_lst_person():
            if isinstance(person, Doctor):
                lst.append(person.get_yob())
        average = sum(lst)/len(lst)
        print(f"Average year of birth (teachers): {average}")
        return average


class Student(Ward):
    def __init__(self, name, yob, grade):
        self.__name = name
        self.__yob = yob
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_yob(self):
        return self.__yob

    def get_grade(self):
        return self.__grade

    def describe(self):
        return f"Student - name: {self.get_name()} - YoB: {self.get_yob()} - Grade: {self.get_grade()}"

    def __str__(self):
        return f"Student - name: {self.get_name()} - YoB: {self.get_yob()} - Grade: {self.get_grade()}"


class Teacher(Ward):
    def __init__(self, name, yob, subject):
        self.__name = name
        self.__yob = yob
        self.__subject = subject

    def get_name(self):
        return self.__name

    def get_yob(self):
        return self.__yob

    def get_subject(self):
        return self.__subject

    def describe(self):
        return f"Teacher - name: {self.get_name()} - YoB: {self.get_yob()} - Subject: {self.get_subject()}"

    def __str__(self):
        return f"Teacher - name: {self.get_name()} - YoB: {self.get_yob()} - Subject: {self.get_subject()}"


class Doctor(Ward):
    def __init__(self, name, yob, specialist):
        self.__name = name
        self.__yob = yob
        self.__specialist = specialist

    def get_name(self):
        return self.__name

    def get_yob(self):
        return self.__yob

    def get_specialist(self):
        return self.__specialist

    def describe(self):
        return f"Doctor - name: {self.get_name()} - YoB: {self.get_yob()} - Specialist: {self.get_specialist()}"

    def __str__(self):
        return f"Doctor - name: {self.get_name()} - YoB: {self.get_yob()} - Specialist: {self.get_specialist()}"


if __name__ == "__main__":
    print("Part a:")
    student1 = Student("studentZ2023", 2011, 6)
    print(student1)
    print(student1.describe())
    teacher1 = Teacher("teacherZ2023", 1991, "History")
    print(teacher1)
    print(teacher1.describe())
    doctor1 = Doctor("doctorZ2023", 1981, "Endocrinoologists")
    print(doctor1)
    print(doctor1.describe())
    print("-"*100)
    print("\n")
    print("Part b:")
    ward1 = Ward("Ward1")
    teacher2 = Teacher("teacher02", 1965, "Literature")
    doctor2 = Doctor("doctor2", 1990, "Cardiologists")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()
    print("-"*100)
    print("\n")
    print("Part c:")
    ward1.count_doctor()
    print("-"*100)
    print("\n")
    print("Part d:")
    ward1.sort_age()
    ward1.describe()
    print("-"*100)
    print("\n")
    ward1.compute_average()
    