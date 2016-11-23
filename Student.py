class Student:

    def __init__(self, student_id=None, name=None, last_name=None, gender=None, nationality=None):
        self.__student_id = student_id
        self.__name = name
        self.__last_name = last_name
        self.__gender = gender
        self.__nationality = nationality

    def get_student(self):
        return '{} {} with student ID: {} is {} and comes from {}'.format(self.__name, self.__last_name,
                                                                          self.__student_id, self.__gender,
                                                                          self.__nationality)

    def get_nat(self):
        return self.__nationality

    def get_gender(self):
        return self.__gender
