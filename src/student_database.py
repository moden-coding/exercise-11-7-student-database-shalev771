# Write your solution here
def add_student(database: dict, student: str):

    pass


def print_student(database: dict, student: str):
    default = "no completed courses" #default is zero, when student is added but no courses completed
    
    if student in database:
        print(f"{student}:") # start by printing name

        if database[student] == "":
            database[student] = default
            print(" " + str(database[student]))  #if no courses, assisnt with the default value and print

        else:
            if len(database[student]) > 0: #if more than one course, print amount of courses
                average = 0
                print(" " + str(len(database[student])) + " completed courses:") 

                for key, value in database[student]: 
                    print(f"  {key} {value}") # print course name and grade obtained
                    average += value
                if average > 0:
                    average = average / len(database[student])
                    print(" average grade", average) # print average grade for student
            else:
                print(" "+ default)

    else:
        print(f"{student}: no such person in the database") #if name not in database



def add_course(database: dict, student: str, course: tuple):


    pass


def summary(database: dict):
    pass


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")

    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Introduction to Programming", 2))

    add_course(students, "Peter", ("Data Structures and Algorithms", 0))

    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Peter")
    summary(students)
