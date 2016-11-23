import datetime
import os
import sys
import Student as std
import Team as tm

teams = []
colors = ['Naranja', 'Rojo', 'Amarillo', 'Verde', 'Morado']


def fill_teams():
    expected = 0
    num_teams = 0
    while expected <= 0:
        expected = int(input("Number of expected students: "))

    while num_teams <= 0 or num_teams > 9:
        num_teams = int(input("Number of teams per color: "))
    for c in range(0, 5):
        for i in range(0, num_teams):
            t = tm.Team(expected, num_teams)
            t.set_color(colors[c])
            t.set_num(i+1)
            teams.append(t)


def print_teams():
    for team in teams:
        print(team.get_team())
        print('Members')
        team.print_students()


def new_student():
    print('Enter the new student data')
    student_id = input('ID: ')
    name = input('Name: ')
    last_name = input('Last name: ')
    gender = input('Gender (Male/Female): ')
    nationality = input('Nationality (airport code): ')
    teams[0].add_student(std.Student('A01202727', 'Pancho', 'Nunez', 'Male', 'MEX'))
    s = std.Student(student_id, name, last_name, gender, nationality)

    assign(s)
    return


def assign(s):
    weights = []
    i = 0
    for team in teams:
        w = 0
        students = team.get_list()
        for student in students:
            g = student.get_gender()
            n = student.get_nat()
            if g == s.get_gender():
                w += 1
            if n == s.get_nat():
                w += 1
        weights.append(w)
        print(weights[i])
        i += 1


def menu():
    fill_teams()
    op = 1

    while op != 0:
        print('1. Print teams')
        print('2. New student')
        print('0. End')
        op = int(input())

        if op == 1:
            print_teams()
        elif op == 2:
            new_student()

menu()