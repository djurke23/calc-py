def kalkulator():
    broj1 = float(input("Unesite prvi broj: "))
    operacija = input("Unesite operaciju (+, -, *, /): ")
    broj2 = float(input("Unesite drugi broj: "))

    rezultat = None  # Inicijaliziramo rezultat

    if operacija == "+":
        rezultat = broj1 + broj2
    elif operacija == "-":
        rezultat = broj1 - broj2
    elif operacija == "*":
        rezultat = broj1 * broj2
    elif operacija == "/":
        if broj2 != 0:
            rezultat = broj1 / broj2
        else:
            rezultat = "Nije moguće dijeliti s nulom"
    else:
        rezultat = "Nepoznata operacija"

    print(f"Rezultat: {rezultat}")


# Pokrenimo kalkulator
kalkulator()
