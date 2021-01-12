import random
#assigning these two variable that are supposed to be the amount of questions answered and amount of questions correctly answered
count = 0
correct_count = 0

#input statement for the amount of questions that the student wants to answer
num_of_questions = int(
    input(
        "How many questions do you want to answer? Please do not enter more that a hundred and less than 3: "
    ))

#The student should answer more than 3 questions and less than 100. These two while loops make sure of that.
while num_of_questions > 100:
    print("Error: Please enter a number less than a hundred")
    num_of_questions = int(
        input(
            "\nHow many questions do you want to answer? Please do not enter more that a hundred and less than 3: "
        ))
    if num_of_questions <= 100:
        break
while num_of_questions <= 3:
    print(
        "\n Error: It is required that you answer more that three questions.")
    num_of_questions = int(
        input(
            "\nHow many questions do you want to answer? Please do not enter more that a hundred and less than 3: "
        ))
    if num_of_questions > 3:
        break

#This while loop is the part of the code that asks the arithmetic questions to the student.
while count <= num_of_questions:

    #These two variable are the two random numbers that are used in the math problems
    num = random.randint(1, 50)
    num_2 = random.randint(1, 50)

    #The user inputs an operation that they would like
    operation = input(
        "\nWhat operation do you want to do? Type the sign of the operation. For example type '*' by pressing shift + 8. This does not include division: "
    )

    #These three if statements change the operation depending on the user input of the operation.
    if operation == "+":
        answer = num + num_2
        attempt = int(input(f'What is {num} + {num_2}?: '))

        #This if-else statement checks if the student's input is correct. If not is tells the answer.
        if attempt == answer:
            print("\nNICE JOB! YOU GOT IT RIGHT!!!!")
            correct_count += 1
        else:
            print(
                f"\nSorry, you got it wrong. The correct answer was {answer} Maybe next time :("
            )
    elif operation == "-":

        #These nested if statements inside the subtraction if statement make sure the the answer of the subtraction problem is not negative.
        if num > num_2:
            answer = num - num_2
            attempt = int(input(f"What is {num} - {num_2}?: "))

            #This if-else statement checks if the student's input is correct. If not is tells the answer.
            if attempt == answer:
                print("\nNICE JOB! YOU GOT IT RIGHT!!!!")
                correct_count += 1
            else:
                print(
                    f"\nSorry, you got it wrong. The correct answer was {answer} Maybe next time :("
                )
        if num < num_2:
            answer = num_2 - num

            #This if-else statement checks if the student's input is correct. If not is tells the answer.
            attempt = int(input(f"What is {num_2} - {num}?: "))
            if attempt == answer:
                print("\nNICE JOB! YOU GOT IT RIGHT!!!!")
                correct_count += 1
            else:
                print(
                    f"\nSorry, you got it wrong. The correct answer was {answer} Maybe next time :("
                )

    elif operation == "*":
        answer = num * num_2
        attempt = int(input(f"What is {num} x {num_2}?: "))

        #This if-else statement checks if the student's input is correct. If not is tells the answer.
        if attempt == answer:
            print("\nNICE JOB! YOU GOT IT RIGHT!!!!")
            correct_count += 1
        else:
            print(
                f"\nSorry, you got it wrong. The correct answer was {answer} Maybe next time :("
            )
    count += 1
    if count == num_of_questions:
        print(
            f"\n\n\n\nYou got {correct_count} out of {count} problems correct and you got {int(correct_count/count * 100)} percent!"
        )
        break
