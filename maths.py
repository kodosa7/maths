import os, random, assets, time
from sys import platform
from colorama import Fore, Style, Back


RIGHT, WRONG = 0, 0
answerDict = dict()


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
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    while num1 <= num2:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
    if meth == "/" or meth == "*":  # if / or * is used, generate low num2
        num2 = random.randint(1, 11)
    return num1, num2

def wait(pause):
    time.sleep(pause)

def askUser(meth, num1, num2, quest):
    global RIGHT
    global WRONG
    print(f"\n{Fore.BLUE}Questions to go:{Fore.LIGHTYELLOW_EX}", quest, f"{Style.RESET_ALL}")
    answer = input(f"    {Fore.LIGHTWHITE_EX}" + str(num1) + " " + meth + " " + str(num2) + f" = {Style.RESET_ALL}")
    if int(answer) == calc.countNumbers():
        print(f"{Fore.LIGHTGREEN_EX}--> Correct \o/{Style.RESET_ALL}")
        RIGHT += 1
        wait(.5)
        answerDict[str(num1) + " " + meth + " " + str(num2) + " = " + str(answer) + " -> "] = "ok"
    else:
        print(f"{Fore.LIGHTRED_EX}... WRONG! :-({Style.RESET_ALL}")
        wait(.5)
        print(f"{Fore.LIGHTCYAN_EX}--> The correct answer is {Fore.LIGHTWHITE_EX}{str(calc.countNumbers())}{Style.RESET_ALL}")
        WRONG += 1
        wait(.5)
        answerDict[str(num1) + " " + meth + " " + str(num2) + " = " + str(answer) + " -> "] = "error"

def osCheckAndClearScreen():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
        
def showLogo():
    for line in assets.logo:
        print(line)

def intro():
    osCheckAndClearScreen()
    showLogo()
    howManyQuestions = int(input("\nHello :) How many calculations do you want? (1 to 99): "))
    if 1 <= howManyQuestions < 100:
        return howManyQuestions
    else:
        print("Answer out of range 1-99")
        quit()

def conclusion(quest):
    global RIGHT
    global WRONG

    print(f"\n{Fore.CYAN}Today's Calculations:{Style.RESET_ALL}")
    for key, value in answerDict.items():
        if value == "error":
            print(f"    {Fore.WHITE}{key}{Fore.LIGHTRED_EX}{value}{Style.RESET_ALL}")
        else:
            print(f"    {Fore.WHITE}{key}{Fore.LIGHTGREEN_EX}{value}{Style.RESET_ALL}")

    print(f"\nYou have answered {str(quest)} questions.")
    print(f"You answered {str(RIGHT)} right answers and made {str(WRONG)} mistakes.")

    if WRONG == 0:
        print(f"\n{Fore.LIGHTCYAN_EX}Congratulations!{Style.RESET_ALL}\n")
    else:
        print(f"\n{Fore.LIGHTMAGENTA_EX}Better luck next time!{Style.RESET_ALL}\n")

if __name__ == "__main__":
    questions = intro()
    questionsStartedWith = questions

    while questions in range(1, 100):
        method = generateRandomMethod()
        number1, number2 = generateRandomNumbers(method)

        calc = Calculate(method, number1, number2)

        askUser(method, number1, number2, questions)
        questions -= 1

    conclusion(questionsStartedWith)
