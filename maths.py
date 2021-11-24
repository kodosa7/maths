import os, random


RIGHT, WRONG = 0, 0


class Calculate:
    def __init__(self, method, num1, num2):
        self.method = method
        self.num1 = num1
        self.num2 = num2
        
    def countNumbers(self):
        if method == "+":
            return self.num1 + self.num2
        if method == "-":
            return self.num1 - self.num2
        if method == "*":
            return self.num1 * self.num2
        if method == "/":
            return self.num1 // self.num2


def generateRandomMethod():
    randMethodNum = random.randint(0, 3)
    if randMethodNum == 0:
        return "+"
    if randMethodNum == 1:
        return "-"
    if randMethodNum == 2:
        return "*"
    if randMethodNum == 3:
        return "/"

def generateRandomNumbers(meth):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    while num1 <= num2:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    if meth == "/" or meth == "*":  # if / or * is used, generate low num2
        num2 = random.randint(1, 11)
    return num1, num2

def askUser(meth, num1, num2):
    global RIGHT
    global WRONG
    answer = input("\n    " + str(num1) + " " + meth + " " + str(num2) + " = ")
    if int(answer) == calc.countNumbers():
        print("--> Correct \o/")
        RIGHT += 1
    else:
        print(f"--> Wrong! ._. The correct answer is {str(calc.countNumbers())}")
        WRONG += 1

def intro():
    os.system("cls")
    print("""
This is counting program
for all children wanting to learn to count
    """)
    howManyQuestions = int(input("How many questions would you like? "))
    return howManyQuestions

def conclusion(quest):
    global RIGHT
    global WRONG
    print(f"\nYou have answered {str(quest)} questions.")
    print(f"You answered {str(RIGHT)} right answers and made {str(WRONG)} mistakes.")
    if WRONG == 0:
        print("Congratulations!")
    else:
        print("Better luck next time!")
    print()

if __name__ == "__main__":
    questions = intro()
    questionsStartedWith = questions

    while questions > 0:
        method = generateRandomMethod()
        number1, number2 = generateRandomNumbers(method)

        calc = Calculate(method, number1, number2)

        askUser(method, number1, number2)
        questions -= 1

    conclusion(questionsStartedWith)
