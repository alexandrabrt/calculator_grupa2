# list = ["+", "-", "*", "/"]
# continua = "DA"
# while continua == "DA":
#
#
#     numar1 = input("Primul numar:\n")
#     operatia = input("Ce operatie vrei sa faci (+, -, *, /):\n")
#     numar2 = input("Al doilea numar:\n")
#
#     numar1 = float(numar1)
#     numar2 = float(numar2)
#
#     rezultat = None
#
#     if operatia in list:
#         if operatia == "+":
#             rezultat = numar1 + numar2
#         elif operatia == "-":
#             rezultat = numar1 - numar2
#         elif operatia == "*":
#             rezultat = numar1 * numar2
#         elif operatia == "/" and numar2 != 0:
#             rezultat = numar1 / numar2
#     if rezultat is None:
#         print("Nu se poate realiza impartirea la zero!")
#     else:
#         print("Rezultat este:" + str(rezultat))
#     continua = input("Vrei sa reiei operatia? ").upper()
#


def adunare(numar1: int, numar2: int) -> int:
    return numar1 + numar2


def scadere(numar1: int, numar2: int) -> int:
    return numar1 - numar2


def inmultire(numar1: int, numar2: int) -> int:
    return numar1 * numar2


def impartire(numar1: int, numar2: int) -> float:
    return numar1 / numar2





def main():
    global rezultat
    numar_ales_1 = int(input("Introduceti primul numar: "))
    numar_ales_2 = int(input("Introduceti al doilea numar: "))
    operatia = input("Selectati operatia dorita: ")
    if operatia == "+":
        rezultat = adunare(numar_ales_1, numar_ales_2)
    elif operatia == "-":
        rezultat = scadere(numar_ales_1, numar_ales_2)
    elif operatia == "*":
        rezultat = inmultire(numar_ales_1, numar_ales_2)
    elif operatia == "/":
        if numar_ales_2 == 0:

            rezultat = None
        else:

            rezultat = impartire(numar_ales_1, numar_ales_2)

    return rezultat


continua = 'DA'
while continua == 'DA':

    a = main()
    if a == None:
        print("Nu se poate realiza impartirea la zero ")
    else:
        print(a)
    continua = input("Vrei sa reiei operatia? ").upper()