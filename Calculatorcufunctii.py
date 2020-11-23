# # list = ["+", "-", "*", "/"]
# # continua = "DA"
# # while continua == "DA":
# #
# #
# #     numar1 = input("Primul numar:\n")
# #     operatia = input("Ce operatie vrei sa faci (+, -, *, /):\n")
# #     numar2 = input("Al doilea numar:\n")
# #
# #     numar1 = float(numar1)
# #     numar2 = float(numar2)
# #
# #     rezultat = None
# #
# #     if operatia in list:
# #         if operatia == "+":
# #             rezultat = numar1 + numar2
# #         elif operatia == "-":
# #             rezultat = numar1 - numar2
# #         elif operatia == "*":
# #             rezultat = numar1 * numar2
# #         elif operatia == "/" and numar2 != 0:
# #             rezultat = numar1 / numar2
# #     if rezultat is None:
# #         print("Nu se poate realiza impartirea la zero!")
# #     else:
# #         print("Rezultat este:" + str(rezultat))
# #     continua = input("Vrei sa reiei operatia? ").upper()
# #
#
#
# def adunare(numar1: int, numar2: int) -> int:
#     """
#
#     :param numar1: Primul numar introdus de la tastatura
#     :param numar2: Al doilea numar introdus de la tastatura
#     :return: Suma celor doua numere
#     """
#     return numar1 + numar2
#
#
# def scadere(numar1: int, numar2: int) -> int:
#     """
#
#     :param numar1: Primul numar introdus de la tastatura
#     :param numar2: Al doilea numar introdus de la tastatura
#     :return: Diferenta celor doua numere
#     """
#     return numar1 - numar2
#
#
# def inmultire(numar1: int, numar2: int) -> int:
#     """
#
#     :param numar1: Primul numar introdus de la tastatura
#     :param numar2: Al doilea numar introdus de la tastatura
#     :return: Inmultirea celor doua numere
#     """
#     return numar1 * numar2
#
#
# def impartire(numar1: int, numar2: int) -> float:
#     """
#
#     :param numar1: Primul numar introdus de la tastatura
#     :param numar2: Al doilea numar introdus de la tastatura
#     :return: Impartirea celor doua numere
#     """
#     return numar1 / numar2
#
#
# def main() -> float:
#     rezultat = None
#     numar_ales_1 = int(input("Introduceti primul numar: "))
#     numar_ales_2 = int(input("Introduceti al doilea numar: "))
#     operatia = input("Selectati operatia dorita: ")
#     if operatia == "+":
#         rezultat = adunare(numar_ales_1, numar_ales_2)
#     elif operatia == "-":
#         rezultat = scadere(numar_ales_1, numar_ales_2)
#     elif operatia == "*":
#         rezultat = inmultire(numar_ales_1, numar_ales_2)
#     elif operatia == "/" and numar_ales_2 != 0:
#         rezultat = impartire(numar_ales_1, numar_ales_2)
#
#     return rezultat
#
#
# continua = 'DA'
# while continua == 'DA':
#
#     a = main()
#     if a is None:
#         print("Nu se poate realiza impartirea la zero ")
#     else:
#         print(a)
#     continua = input("Vrei sa reiei operatia? ").upper()



class Calculator:

    def add(self):
        print(a + b)

    def subtr(self):
        print(a - b)

    def multyply(self):
        print(a * b)

    def divide(self):
        print(a / b)

a = int(input("Introduceti primul numar: "))
b = int(input("Introduceti al doilea numar: "))

obj = Calculator()

alegere = 1
while alegere != 0:
    print("1. Adunare")
    print("2. Scadere")
    print("3. Inmultire")
    print("4. Impartire")
    alegere = int(input("Alegeti operatia dorita"))
    if alegere == 1:
        print(obj.add())
    elif alegere == 2:
        print(obj.subtr())
    elif alegere == 3:
        print(obj.multyply())
    elif alegere == 4:
        print(obj.divide())
    else:
        print("Operatie Invalida ")

