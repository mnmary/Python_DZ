class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return f"Преподаватель {lecturer.name} {lecturer.surname} не является лектором"

        if not course in self.courses_in_progress:
            return f"Студент {self.name} {self.surname} не слушает курс {course}"

        elif not course in lecturer.courses_attached:
            return f"Лектор {lecturer.name} {lecturer.surname} не закреплен за курсом {course}"

        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise "other не является классом Student"
        return self.get_average() == other.get_average()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise "other не является классом Student"
        return self.get_average() > other.get_average()

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise "other не является классом Student"
        return self.get_average() < other.get_average()

    def get_average(self):
        sum_grade = 0
        count_grades = 0
        for course in self.grades:
            sum_grade += sum(self.grades[course])
            count_grades += len(self.grades[course])
        if count_grades > 0:
            return sum_grade/count_grades
        else:
            return 0

    def get_average_course(self, course):
        sum_grade = 0
        count_grades = 0
        sum_grade += sum(self.grades[course])
        count_grades += len(self.grades[course])
        if count_grades > 0:
            return sum_grade/count_grades
        else:
            return 0

    def __str__(self):
        quan = self.get_average()
        return f"Имя: {self.surname}\n" + f"Фамилия: {self.name}\n" + f"Средняя оценка за домашнее задание: {quan}\n"+ f"Курсы в процессе: {', '.join(self.courses_in_progress)}\n" + f"Завершенные курсы: {','.join(self.finished_courses)}\n"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average(self):
        sum_grade = 0
        count_grades = 0
        for course in self.grades:
            sum_grade += sum(self.grades[course])
            count_grades += len(self.grades[course])
        if count_grades > 0:
            return sum_grade/count_grades
        else:
            return 0

    def get_average_course(self, course):
        sum_grade = 0
        count_grades = 0
        sum_grade += sum(self.grades[course])
        count_grades += len(self.grades[course])
        if count_grades > 0:
            return sum_grade/count_grades
        else:
            return 0

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise "other не является классом Lecturer"
        return self.get_average() == other.get_average()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise "other не является классом Lecturer"
        return self.get_average() > other.get_average()


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise "other не является классом Lecturer"
        return self.get_average() < other.get_average()

    def __str__(self):
        quan = self.get_average()
        return f"Имя: {self.name}\n" + f"Фамилия: {self.surname}\n" + f"Средняя оценка за лекции: {quan}\n"

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n" + f"Фамилия: {self.surname}\n"

#1
#lecturer = Lecturer('Иван', 'Иванов')
#reviewer = Reviewer('Пётр', 'Петров')
#print(isinstance(lecturer, Mentor)) # True
#print(isinstance(reviewer, Mentor)) # True
#print(lecturer.courses_attached)    # []
#print(reviewer.courses_attached)    # []

#2
#lecturer = Lecturer('Иван', 'Иванов')
#reviewer = Reviewer('Пётр', 'Петров')
#student = Student('Алёхина', 'Ольга', 'Ж')

#student.courses_in_progress += ['Python', 'Java']
#lecturer.courses_attached += ['Python', 'C++']
#reviewer.courses_attached += ['Python', 'C++']

#print(student.rate_lecture(lecturer, 'Python', 7))  # None
#print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
#print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
#print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

#print(lecturer.grades)  # {'Python': [7]}

#3
student = Student('Алёхина', 'Ольга', 'Ж')
student.courses_in_progress += ['Python', 'Java']

reviewer = Reviewer('Пётр', 'Петров')
reviewer.courses_attached += ['Python', 'Java']

reviewer.rate_hw(student, 'Python', 4)
reviewer.rate_hw(student, 'Python', 5)

reviewer.rate_hw(student, 'Java', 4)
reviewer.rate_hw(student, 'Java', 3)
reviewer.rate_hw(student, 'Java', 3)

lecturer = Lecturer('Иван', 'Иванов')
lecturer.courses_attached += ['Python', 'Java']

student.rate_lecture(lecturer, 'Python', 7)
student.rate_lecture(lecturer, 'Java', 8)

print(student)
print(reviewer)
print(lecturer)

#3.1
lecturer1 = Lecturer('Иван', 'Сидоров')
lecturer1.courses_attached += ['Python', 'Java']

student.rate_lecture(lecturer1, 'Python', 8)
student.rate_lecture(lecturer1, 'Java', 8)
print(lecturer1)

print(lecturer1 > lecturer)

student1 = Student('Алёхин', 'Михаил', 'М')
student1.courses_in_progress += ['Python', 'Java']
reviewer.rate_hw(student1, 'Python', 4)
reviewer.rate_hw(student1, 'Java', 5)
print(student1)

print(student1 > student)

#4
def calc_avg_student(students, course):
    sum_rate = 0
    for stud in students:
        sum_rate += stud.get_average_course(course)
    len_rate = len(students)
    if len_rate > 0:
        return sum_rate/len_rate
    else:
        return 0

def calc_avg_lectern(lecterns, course):
    sum_rate = 0
    for lect in lecterns:
        sum_rate += lect.get_average_course(course)
    len_rate = len(lecterns)
    if len_rate > 0:
        return sum_rate/len_rate
    else:
        return 0

print("%.1f" % calc_avg_student([student1, student],"Java"))
print('%.1f' % calc_avg_lectern([lecturer1, lecturer],"Java"))
