list = ["+", "-", "*", "/"]
continua = "DA"
while continua == "DA":


    numar1 = input("Primul numar:\n")
    operatia = input("Ce operatie vrei sa faci (+, -, *, /):\n")
    numar2 = input("Al doilea numar:\n")

    numar1 = float(numar1)
    numar2 = float(numar2)

    rezultat = None

    if operatia in list:
        if operatia == "+":
            rezultat = numar1 + numar2
        elif operatia == "-":
            rezultat = numar1 - numar2
        elif operatia == "*":
            rezultat = numar1 * numar2
        elif operatia == "/" and numar2 != 0:
            rezultat = numar1 / numar2
    if rezultat is None:
        print("Nu se poate realiza impartirea la zero!")
    else:
        print("Rezultat este:" + str(rezultat))
    continua = input("Vrei sa reiei operatia? ").upper()