class Team:

    def __init__(self, expected=None, team_color=None):
        self.__students = []
        self.__team_size = self.ceildiv(expected, (5 * team_color))
        self.__team_size = None
        self.__color = None
        self.__number = None

    def ceildiv(self, a, b):
        return -(-a // b)

    def get_max(self):
        return self.__team_size

    def set_color(self, color):
        self.__color = color

    def set_num(self, num):
        self.__number = num

    def get_team(self):
        return 'Team {} {} has {} of {} possible members'.format(self.__color, self.__number,
                                                                 self.get_students(), self.__team_size)

    def get_students(self):
        return len(self.__students)

    def is_full(self):
        return len(self.__students) == self.__team_size

    def add_student(self, s):
        self.__students.append(s)

    def print_students(self):
        for student in self.__students:
            print(student.get_student())

    def get_list(self):
        return self.__students
