from time import *
import threading

def countdown():
    global my_timer

    my_timer = 500

    for x in range(500) :
        my_timer = my_timer - 1
        sleep(1)
    print("Out of time")

countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()
name = input('Please type your name:')
print('Hello,', name)
score = 0
while my_timer > 0:
    print("Quiz I. Identify what is being asked in the following sentences")
    # We use a scanner so that the player can write his or her answer.
    question1 = input("1. What programming language can handle big data and perform complex mathematics? ")

    if question1 == "Python":
        print("Correct")
        score = score + 1
    elif question1 == "python":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    question2 = input("2. Who is the creator of python? ")
    if question2 == "Guido Van Rossum":
        print("Correct")
        score = score + 1
    elif question2 == "Guido van Rossum":
        print("Correct")
        score = score + 1

    elif question2 == "guido van rossum":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    question3 = input("3. What operator is used to multiply numbers? ")
    if question3 == "*":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    question4 = input("4. What statement is used to stop a loop? ")
    if question4 == "break":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    question7 = input("5. What is a correct syntax to output \"Hello World\" in Python? ")
    if question7 == "print(\"Hello World\")":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")


    print("Quiz II. Multiply")

    question7 = input("6.What year was python released? \n a) 1993. b) 1991. c) 1992: ")

    if question7 == "b":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    question8 = input("7. Is Python case sensitive when dealing with identifiers? \n a) yes b) no :  ")
    if question8 == "b":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    question9 = input("8. Who developed Python Programming Language? \n a) Wick van Rossum b) Rasmus Lerdorf c) Guido van Rossum d) Niene Stom  :   ")
    if question9 == "c":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    question10 = input("9. Which of the following is the correct extension of the Python file?  \n a) .python b) .pl c) .py d) .p : ")
    if question10 == "c":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")

    question11 = input("10. Which type of Programming does Python support? \n a) object-oriented programming b) structured programming c) functional programming d) all of the mentioned :")
    if question11 == "d":
        print("Correct")
        score = score + 1
    else:
        print("Wrong")


    if score >= 7:
        print("Congratulations, your score is " + str(score) + "/10")
    else:
        print("Better luck next time, your score is " + str(score) + "/10")
    break

