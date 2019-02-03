
# NO PEEKING AT THE PROJECT CODE BEFORE RUNNING IT
# DON'T CHEAT!!
# RUN THE CODE TO VIEW THE PRESENTATION


















































































































































































































































































from time import sleep

def project_presentation():
    print("Welcome to my presentation. The deadline approaches and I find myself running low on time. That is why I have chosen this presentation method.")
    print(" ")
    sleep(3)
    print("There are 5 questions need to be answered according to the instructions.")
    print(" ")
    sleep(1)
    print("Type in the number corresponding with the question you wish to see the answer of.")
    print(" ")
    sleep(1)
    print("Type 1 for the answer to question 1, 2 for question 2 etc.")
    print(" ")
    sleep(1)
    question = input("> ")
    
    if question == '1':
        print("I used a Linked List for part 1.")
        print(" ")
        sleep(1)
        print("There are only so many types of foods so there will always be a relatively small collection of data.")
        print(" ")
        sleep(1)
        print("Therefore the Linked List made sense being the easiest to implement.")
        print(" ")
        sleep(3)
        print("Would you like to see the answer to another question? Enter y for yes or n for no")
        print(" ")
        answer = input("> ")
        if answer == 'y':
            project_presentation()
        elif answer == 'n':
            print("CLOSING PROGRAM")
            sleep(2)
            exit(0)
        else:
            print("INVALID INPUT")
            sleep(2)
            print("CLOSING PROGRAM")
            exit(0)

    elif question == '2':
        print("The runtime of traversing a Linked List is 0(N) as the number of iterations depends on the length of the list.")
        print(" ")
        sleep(1)
        print("If I had used a HashMap for the first part of the project the lookup time would be more efficient.")
        print(" ")
        sleep(1)
        print("However, since that particular dataset will not grow much I didn't see much of a benefit to using the HashMap over the LinkedList for part 1.")
        print(" ")
        sleep(3)
        print("Would you like to see the answer to another question? Enter y for yes and n for no")
        print(" ")
        answer = input("> ")
        if answer == 'y':
            project_presentation()
        elif answer == 'n':
            print("CLOSING PROGRAM")
            sleep(2)
            exit(0)
        else:
            print("INVALID INPUT")
            sleep(2)
            print("CLOSING PROGRAM")
            exit(0)

    elif question == '3':
        print("I used a HashMap for part 2.")
        print(" ")
        sleep(1)
        print("The size of the data sample is significantly larger than in part 1 which calls for something more efficient than a LinkedList.")
        print(" ")
        sleep(1)
        print("Plus more restaurants could be added in the future and the HashMap can efficiently accomodate them all.")
        print(" ")
        sleep(3)
        print("Would you like to see the answer to another question? Enter y for yes and n for no")
        print(" ")
        answer = input("> ")
        if answer == 'y':
            project_presentation()
        elif answer == 'n':
            print("CLOSING PROGRAM")
            sleep(2)
            exit(0)
        else:
            print("INVALID INPUT")
            sleep(2)
            print("CLOSING PROGRAM")
            exit(0)

    elif question == '4':
        print("The runtime of finding a value from a hashmap is 0(1).")
        print(" ")
        sleep(1)
        print("I believe this is the most efficient runtime possible. It is the only constant runtime that I know of.")
        print(" ")
        sleep(3)
        print("Would you like to see the answer to another question? Enter y for yes and n for no")
        print(" ")
        answer = input("> ")
        if answer == 'y':
            project_presentation()
        elif answer == 'n':
            print("CLOSING PROGRAM")
            sleep(2)
            exit(0)
        else:
            print("INVALID INPUT")
            sleep(2)
            print("CLOSING PROGRAM")
            exit(0)

    elif question == '5':
        print("There are all kinds of possibilities.")
        print(" ")
        sleep(1)
        print("Data structures could be used for everything from organizing a digital library to implementing various sorting algorithms that may use stacks to keep track of values.")
        print(" ")
        sleep(1)
        print("Graph searching algorithms also seem to utilize data structures such as heaps to keep track of vertices that have already been visited.")
        print(" ")
        sleep(3)
        print("Would you like to see the answer to another question? Enter y for yes and n for no")
        print(" ")
        answer = input("> ")
        if answer == 'y':
            project_presentation()
        elif answer == 'n':
            print("CLOSING PROGRAM")
            sleep(2)
            exit(0)
        else:
            print("INVALID INPUT")
            sleep(2)
            print("CLOSING PROGRAM")
            exit(0)

    else:
        print("Input must be between 1 and 5. Try again.")
        project_presentation()

project_presentation()
    
          
