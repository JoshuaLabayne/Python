from time import *
import threading

name = input('Please type your name:')
print('Hello,', name)


def countdown():
    global my_timer

    my_timer = 130

    for x in range(my_timer):
        my_timer = my_timer - 1
        sleep(1)
    print("Out of time")


countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()

score = 0
while my_timer > 0:

    # 1

    print("")
    print("Quiz I. Identify what is being asked in the following sentences")
    sleep(.5)
    # We use a scanner so that the player can write his or her answer.
    print("")
    question1 = input("1. What programming language can handle big data and perform complex mathematics? ")
    sleep(.5)

    if question1 == "Python":
        print("Correct")
        score = score + 1
    elif question1 == "python":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    if my_timer == 0:
        break

    # 2

    print("")
    question2 = input("2. Who is the creator of python? ")
    sleep(.5)

    if question2 == "Guido Van Rossum":
        print("Correct")
        score = score + 1
    elif question2 == "Guido van Rossum":
        print("Correct")
        score = score + 1

    if my_timer == 0:
        break

    elif question2 == "guido van rossum":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    if my_timer == 0:
        break

    # 3

    print("")
    question3 = input("3. What operator is used to multiply numbers? ")
    sleep(.5)

    if question3 == "*":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    if my_timer == 0:
        break

    # 4

    print("")
    question4 = input("4. What statement is used to stop a loop? ")
    sleep(.5)

    if question4 == "break":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    if my_timer == 0:
        break

    # 5

    print("")
    question5 = input("5. What is a correct syntax to output \"Hello World\" in Python? ")
    sleep(.5)

    if question5 == "print(\"Hello World\")":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    if my_timer == 0:
        break

    # QUIZ II

    print("")
    print("Quiz II. Please select the correct answer and input the corresponding letter in lowercase.")
    sleep(1.5)

    # 6

    print("")
    print("6.What year was python released?")
    print(" a) 1993")
    print(" b) 1991")
    print(" c) 1992")
    question6 = input("Type your answer here: ")
    sleep(1)

    if question6 == "b":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    if my_timer == 0:
        break

    # 7

    print("")
    print("7. Is Python case sensitive when dealing with identifiers?")
    print(" a) yes")
    print(" b) no")
    question7 = input("Type your answer here: ")
    sleep(1)

    if question7 == "b":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    if my_timer == 0:
        break

    # 8

    print("")
    print("8. Who developed Python?")
    print(" a) Niene Stom")
    print(" b) Rasmus Lerdorf")
    print(" c) Guido van Rossum")
    question8 = input("Type your answer here: ")
    sleep(1)

    if question8 == "c":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    if my_timer == 0:
        break

    # 9

    print("")
    print("9. Which of the following is the correct extension of the Python file?")
    print(" a) .p")
    print(" b) .python")
    print(" c) .py")
    question9 = input("Type your answer here: ")
    sleep(1)

    if question9 == "c":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    if my_timer == 0:
        break

    # 10

    print("")
    print("10. Which type of Programming does Python support?")
    print(" a) object-oriented programming")
    print(" b) structured programming")
    print(" c) functional programming")
    print(" d) all of the mentioned")
    question10 = input("Type your answer here: ")
    sleep(1)

    if question10 == "d":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    if my_timer == 0:
        break

    # FINAL SCORE

    if score >= 7:
        print("Congratulations, " + name + ", your score is " + str(score) + "/10")
        sleep(1)
    else:
        print("Better luck next time, " + name + ", your score is " + str(score) + "/10")
        sleep(1)