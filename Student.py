class Student:

    def __init__(self, student_id, name, last_name, gender, nationality):
        self.__student_id = student_id
        self.__name = name
        self.__last_name = last_name
        self.__gender = gender
        self.__nationality = nationality

    def get_student(self):
        return '{} {} with student ID: {} is {} and comes from {}'.format(self.__name, self.__last_name,
                                                                          self.__student_id, self.__gender,
                                                                          self.__nationality)

    def nat(self):
        return self.__nationality

    def gen(self):
        return self.__gender
