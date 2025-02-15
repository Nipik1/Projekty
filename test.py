def jmeno():
    while True:
        jmeno = len(input("Zadejte svoje jméno: "))
        if jmeno < 3:
            print("Jméno je příliš krátké")
            continue
        elif jmeno > 15:
            print("Jméno je příliš dlouhé")
            continue
        else:
            print("V pořádku, můžete pokračovat.")
            break

import time
import string
import random

def PyPassword():
    print("Vítejte v generátoru hesla")
    time.sleep(1)
    abeceda = string.ascii_letters
    cisla = string.digits
    znaky = string.punctuation

    rn_abeceda = 4
    rn_cisla = 3
    rn_znaky = 2

    heslo = []

    for _ in range(rn_abeceda):
        heslo.append(random.choice(abeceda))
    for _ in range(rn_cisla):
        heslo.append(random.choice(cisla))
    for _ in range(rn_znaky):
        heslo.append(random.choice(znaky))

    random.shuffle(heslo)
    print("Heslo se generuje...")
    time.sleep(1)
    print(f"Vaše nové heslo je {''.join(heslo)}")


def kalkulacka():
    print("Děkujeme za prihlášení. Nyní můžeme pokračovat ke kalkulačce")
    time.sleep(1)

    while True:
        try:
            prvni_cislo = float(input("Zadejte první číslo: "))
            druhe_cislo = float(input("Zadeje druhé číslo: "))
        except ValueError:
            print("Neplatný vstup. Prosím zkuste to znovu")
            continue

        operace = ["+", "-", "*", "/"]
        rn_operace = input("Prosím zadejte matematickou operaci + - * /: ").strip()
        if rn_operace not in operace:
            print("Neplatný vstup. Použíjte + - * nebo /")
            continue

        if rn_operace == "/" and druhe_cislo == 0:
            print("Nelze dělit nulou, zkuste to prosím znovu.")
            continue

        if rn_operace == "+":
            vysledek = (prvni_cislo + druhe_cislo)
        elif rn_operace == "-":
            vysledek = (prvni_cislo - druhe_cislo)
        elif rn_operace == "*":
            vysledek = (prvni_cislo * druhe_cislo)
        elif rn_operace == "/":
            vysledek = (prvni_cislo / druhe_cislo)
        
        print(f"{prvni_cislo} {rn_operace} {druhe_cislo} = {vysledek}")

        pokracovat = input("Přejete si pokračovat? Y/N: ").lower()
        if pokracovat == "y":
            continue
        else:
            print("Děkujeme a hezký den")
            break


def main():

    jmeno()

    while True:
        try:
            volba = input("Vyberte jaký program chcete spustit (1) Generátor hesla nebo (2) Kalkulačka nebo (3) pro ukončení: ")
            if volba == "1":
                PyPassword()
            elif volba == "2":
                kalkulacka()
            elif volba == "3":
                print("Děkujeme a přejeme hezký den")
                break
            else:
                print("Neplatná volba. Prosím zkuste to znovu")
                continue
        except ValueError:
            print("Neplatná volba.")

    
main()