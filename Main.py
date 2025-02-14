import random
import string
import time

def PyPassword():

    abeceda = string.ascii_letters
    cisla = string.digits
    znaky = string.punctuation

    print("Vítejte v PyPassword Generátoru")
    time.sleep(1)

    while True:
        try:
            rn_abeceda = int(input("Zadejte kolik chcete, aby vaše heslo mělo písmen: "))
            rn_cisla = int(input("Zadejte kolik chcete, aby vaše heslo mělo čísel: "))
            rn_znaky = int(input("Zadejte kolik chcete, aby vaše heslo mělo znaků: "))
            break
        except ValueError:
            print("Neplatný vstup. Prosím zkuste napsat číslo")
            continue
    
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

def jmeno():
    
    while True:
        uzivatel = input("Zadejte prosím svoje jméno: ")
        if len(uzivatel) < 3:
            print("Jméno je příliš krátké")
        elif len(uzivatel) > 15:
            print("Jméno je příliš dlouhé")
        else:
            print("V pořádku, prosím pokračujte na generátor hesla.")
            break

def main():
    jmeno()
    time.sleep(1)
    PyPassword()

if __name__ == "__main__":
    main()

main()