"""
Desarrolla un programa en Python que permita registrar y gestionar las notas de
varios estudiantes. El sistema debe cumplir las siguientes funcionalidades básicas:

    ● Agregar estudiantes: El usuario podrá ingresar el nombre de un estudiante y sus
    tres notas (valores entre 0 y 10).
    ● Quitar estudiantes: El usuario podrá eliminar un registro de un estudiante dado el
    nombre.
    ● Mostrar estudiantes aprobados: Mostrar solo los estudiantes cuyo promedio sea mayor o igual a 6.
    ● Buscar estudiante por nombre y mostrar su promedio.
    ● Mostrar todos los estudiantes con sus promedios.
    ● Salir del programa.

Subir el programa a su repositorio remoto GIT.

"""
from utils import get_marks, average_list

students = {}

def add_student():
    """
    Adds a key in the student dictionary by name and 3 marks.
    TODO: Avoid adding students with the same name.
    """
    while True:
        name = input("Please insert students name: ")
        if name in students:
            print(f"{name} is already created, please enter a different name.")
        else:
            students[name] = get_marks()
            break

def remove_student():
    """
    Removes a student from the students dictionary.
    """
    name = input("Please insert students name: ")
    if name in students:
        students.pop(name)
        print(f"{name} has been removed.")
    else:
        print(f"{name} is not a student.")

def get_pass_students():
    """
    Calls average_list to calculate average for every student and returns a list of tuples name, average.
    """
    pass_students = []
    for student, marks in students.items():
        average = average_list(marks)
        if average >= 6:
            pass_students.append((student, average))
    return pass_students

def show_average_student():
    pass

def get_all_students_average():
    averages = []
    for student, marks in students.items():
        averages.append((student, average_list(marks)))
    return averages


def print_menu():
    print("\n--- NAVIGATION ---")
    print("1 - Add student")
    print("2 - Remove student")
    print("3 - Show passing students")
    print("4 - Search student and show average")
    print("5 - Show all students and their average")
    print("6 - Quit\n")

def main():
    print("Welcome to your students database.")

    while True:
        print_menu()
        option = input("Type a number from 1 to 6 to proceed: ")

        if option not in "123456":
            print(">>> Invalid option. Please, try again.\n")

        elif option == "1":
            add_student()

        elif option == "2":
            remove_student()

        elif option == "3":
            pass_students = get_pass_students()
            print("Passing students: ")
            if pass_students:
                print("   Name | Average")
                i = 1
                for student in pass_students:
                    print(f"{i} - {student[0]} | {student[1]:.2f}")
                    i += 1
            else:
                print("None")

        elif option == "4":
            show_average_student()

        elif option == "5":
            averages = get_all_students_average()
            print("\nName | Average")
            for student in averages:
                print(f"{student[0]} | {student[1]:.2f}")

        elif option == "6":
            print("Program exited.")
            break

if __name__ == "__main__":
    main()