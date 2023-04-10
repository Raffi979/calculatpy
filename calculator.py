def sum(number1, number2):
    print("Enter first number")
    number1 = int(input())
    print("Enter second number")
    number2 = int(input())
    print()
    print(number1+number2)

def divide(number1, number2):
    print("Enter first number")
    number1 = int(input())
    print("Enter second number")
    number2 = int(input())
    print()
    print(number1/number2)

def multiple(number1, number2):
    print("Enter first number")
    number1 = int(input())
    print("Enter second number")
    number2 = int(input())
    print()
    print(number1*number2)

def subtract(number1, number2):
    print("Enter first number")
    number1 = int(input())
    print("Enter second number")
    number2 = int(input())
    print()
    print(number1-number2)
while True:
    print("=======  MENU  =======")
    print("{ 1 } Sum")
    print("{ 2 } Divide")
    print("{ 3 } Multiple")
    print("{ 4 } Subtract")
    print("{ 5 } Settings")
    print("{ 00 } Exit")
    print()
    print("Select an option")
    x = input()

    if x == "1":
        print()
        print("+++++++ SUM +++++++")
        sum(0, 0)
    elif x == "2":
        print()
        print("/////// DIVIDE ///////")
        divide(0, 0)
    elif x == "3":
        print()
        print("******* MULTIPLE *******")
        multiple(0, 0)
    elif x == "4":
        print()
        print("------- MINUS -------")
        subtract(0, 0)
    elif x == "00":
        print(" { - } Exited")
        break
    elif x == "5":
        print()
        print("+-+-+-+-+- SETTINGS +-+-+-+-+-")
        print()
        print("{ 1 } Language")
        print("Select an option")
        y = input()
        if y == "1":
            print("Loading...")
            print("Importing languages available")
            print("SUCCESS!")
            print()
            print("1. Armenia")
            print("2. English (default)")
            print("3. Russian")
            print()
            print("!!!!!!! WARNING !!!!!!!")
            print("You can change language only one time! And every time you restart programm default language will be English!!!")
            print()
            print("Choose an option")
            lang = input()
            if lang == "1":
                print("{+} Wait please while compiling")
                print("{+} This can take few seconds")
                print('{+} SUCCESS')
                print("{+} Language installed")
                print()
                print()
                while True:
                    print("=======  ՄԵՆՅՈՒ  =======")
                    print("{ 1 } Գումարում")
                    print("{ 2 } Բաժանում")
                    print("{ 3 } Բազմապատկում")
                    print("{ 4 } Հանում")
                    print("{ 5 } Պարամետրեր")
                    print("{ 00 } Չեղարկել")
                    print()
                    print("Ընտրեք տարբերակներից մեկը")
                    x = input()

                    if x == "1":
                        print()
                        print("+++++++ ԳՈՒՄԱՐՈՒՄ +++++++")
                        sum(0, 0)
                    elif x == "2":
                        print()
                        print("/////// ԲԱԺԱՆՈՒՄ ///////")
                        divide(0, 0)
                    elif x == "3":
                        print()
                        print("******* ԲԱԶՄԱՊԱՏԿՈՒՄ *******")
                        multiple(0, 0)
                    elif x == "4":
                        print()
                        print("------- ՀԱՆՈՒՄ -------")
                        subtract(0, 0)
                    elif x == "5":
                        print()
                        print("+-+-+-+-+- ՊԱՐԱՄԵՏՐԵՐ +-+-+-+-+-")
                        print()
                        print("Ընտրեք տարբերակներից մեկը")
                        y = input()
                    elif x == "00":
                        break
            if lang == "3":
                print("{+} Wait please while compiling")
                print("{+} This can take few seconds")
                print('{+} SUCCESS')
                print("{+} Language installed")
                print()
                print()
                while True:
                    print("=======  МЕНЮ  =======")
                    print("{ 1 } Сумма")
                    print("{ 2 } Разделять")
                    print("{ 3 } Умножение")
                    print("{ 4 } Вычитание")
                    print("{ 5 } Настройки")
                    print("{ 00 } Отменить")
                    print()
                    print("Выберите один из вариантов")
                    x = input()

                    if x == "1":
                        print()
                        print("+++++++ СУММА +++++++")
                        sum(0, 0)
                    elif x == "2":
                        print()
                        print("/////// РАЗДЕЛЯТЬ ///////")
                        divide(0, 0)
                    elif x == "3":
                        print()
                        print("******* УМНОЖЕНИЕ *******")
                        multiple(0, 0)
                    elif x == "4":
                        print()
                        print("------- ВЫЧИТАНИЕ -------")
                        subtract(0, 0)
                    elif x == "5":
                        print()
                        print("+-+-+-+-+- НАСТРОЙКИ +-+-+-+-+-")
                        print()
                        print("Нет варианта")
                    elif x == "00":
                        break