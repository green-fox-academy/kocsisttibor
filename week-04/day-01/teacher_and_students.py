# Teacher Student

# Create Student and Teacher classes
# Student
# learn()
# question(teacher) -> calls the teachers answer method
# Teacher
# teach(student) -> calls the students learn method
# answer()

class Student:

    def learn(self):
        print("Yaay")


    def question(self, teacher):
        teacher.answer()


class Teacher:

    def answer(self):
        print("Do it by yourself")


    def teach(self, student):
        student.learn()

kathy = Student()
mrs_simson = Teacher()

kathy.learn()
kathy.question(mrs_simson)