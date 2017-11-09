import re


wynik = 0
counter = 0
loop = True


#funkcja wyrzuca wiodace zera z liczb jezeli liczba nie jest zerem
def wywal_zera(element):
    if len(str(element)) > 1:
        return str(element).lstrip("0")
    else:
        return str(element)


#Glowna fukncja do obliczen
def przeliczaj():
    global wynik,counter,loop

    dzialanie = ""
    skladowe = []
    bez_widacych_zer = []


#zeby prompt byl tylko na poczatku, po resecie, po wyniku 0
    if wynik == 0:
        if counter == 0:
            dzialanie = input("Type equation:\n")
        if counter == 1:
            dzialanie = input("Last one evaluated to zero, type next equation:\n")
    else:
        dzialanie = input(str(wynik))

#zabezpieczenie przed brakiem wprowadzenia
    if dzialanie == "":
        print("No input!")

#wyjscie
    elif dzialanie == "quit":
        loop = False
#reset
    elif dzialanie == "c":
        wynik = 0
        counter = 0

#dodanie spacji przed/po liczbach zeby mozna je bylo potem pociac dla funkcji wywalania zer
    else:
        counter = 1
        dzialanie = re.sub('(\\d+)', ' \\1 ', dzialanie)

# wywalam wiodace zera jezeli gdzies sa
        skladowe = dzialanie.split()
        bez_wiodacych_zer = list(map(wywal_zera, skladowe))
        dzialanie = ''.join(bez_wiodacych_zer)

# wywalam litery, znaki specjalne itd
        dzialanie = re.sub('[a-zA-Z,:%$#@!&^()=_" "]','', dzialanie)

#jezel to kolejne dzialanie to przenies do niego wynik poprzedniego
        if wynik == 0:
            wynik = eval(dzialanie)

#Sprawdzenie czy sa tylko dopuszczalne operatory i czy nie ma podwojnych operatorow na poczatku (** jest dozwolone)
        else:
            if str(dzialanie)[0] == "+" or str(dzialanie)[0] == "-" or str(dzialanie)[0] == "/":
                if str(dzialanie)[1] == "-" or str(dzialanie)[1] == "+" or str(dzialanie)[1] == "/" or str(dzialanie)[1] == "*":
                    print("Wrong operator")
                else:
                    wynik = eval(str(wynik) + dzialanie)

            elif str(dzialanie)[0] == "*":
                if str(dzialanie)[1] == "*":
                    wynik = eval(str(wynik) + dzialanie)
                elif str(dzialanie)[1] == "-" or str(dzialanie)[1] == "+" or str(dzialanie)[1] == "/":
                    print("Wrong operator")
            else:
                print("No valid operator")




print("Basic semi fool-proof continuous calculator")
print("Type 'quit' to exit the program. Type 'c' to reset")
print("Calculator will ignore letters, most special characters and will remove any leading zeroes from numbers")


while loop:

    przeliczaj()



