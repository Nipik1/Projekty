import random
import time
import string

users = {}

def get_login():
    print("Vítejne v naši webové aplikaci. Pro pokračování je nutné se registrovat.")
    time.sleep(1)
    while True:
        username_input = input("Zadejte svůj login: ")

        if not username_input:
            print("Zadejte prosím svůj login.")
        elif len(username_input) < 3:
            print("Login je příliš krátký")
        elif len(username_input) > 15:
            print("Login je příliš dlouhý")
        else:
            print("Děkujeme a můžete pokračovat")
            break
    return get_login()

def Generatecode():

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

    new_heslo = ''.join(heslo)
    return new_heslo


def custom_code():

    while True:
        custom_password = input("Zadejte prosím své nové heslo: ")
        if not custom_password:
            print("Zadejte prosím svoje heslo.")
        elif " " in custom_password:
            print("V heslu nesmí být mezera")
        elif custom_password.isnumeric() or custom_password.isalpha():
            print("Heslo musí obsahovat číslo i písmeno.")
        elif len(custom_password) < 6:
            print("Heslo musí mít alespoň 6 znaků.")
        else:
            print("Heslo bylo úspěšně zadáno.")
            break
    return custom_password

def login():

    username = get_login()

    print("Chcete si heslo vytvořit nebo použít generátor hesel?")
    print("=" * 35)
    choice = input("""
    1. Pro generování hesla 
    2. Pro Vlastní heslo
    ---- Vyberte možnost:  """)
    if choice == "1":
        code = Generatecode()
        print(f"Vaše nové heslo je {code}")
    elif choice == "2":
        code = custom_code()
        print(f"Vaše nové heslo je {code}")
    else:
        print("Neplatná volba, zkuste to znovu")
        return login()
    

    users[username] = code

    print(f"Uživatel {username} s heslem {code} byl uložen")

    time.sleep(1)
    print("=" * 20)
    print("Přihlašování...")
    time.sleep(1)
    
    while True:
        login_username = input("Login: ")
        login_code = input("Heslo: ")
        
        if login_username in users and users[login_username] == login_code:
            print(f"Děkujeme za přihlášení {login_username}")
            break
        else:
            print("Neplatné přihlášení, zkute to znovu!")


def kalkulacka():

    print("Vítejte v kalkulačce.")

    while True:
        try:
            first_num = float(input("Zadejte první číslo: "))
        except ValueError:
            print("Zadejte prosím číslo.")
            continue

        operator = input("Zadejte matematický operator + - * nebo /: ")
        seznam_operatoru = ("+", "-", "*", "/")

        if operator not in seznam_operatoru:
            print("Neplatná volba, prosím vyberte + - * nebo /")
            continue
        break

    while True:
        try:
            second_num = float(input("Zadejte druhé číslo: "))
        except ValueError:
            print("Zadejte prosím číslo")
            continue
        if second_num == 0 and operator == "/":
            print("Nelze dělit nulou.")
            continue
        break

    if operator == "+":
        vysledek = first_num + second_num
    elif operator == "-":
        vysledek = first_num - second_num
    elif operator == "*":
        vysledek = first_num * second_num
    elif operator == "/":
        vysledek = first_num / second_num

    print(f"{first_num} {operator} {second_num} = {vysledek}")

    time.sleep(1)

    while True:
        wants_continue = input("Chcete pokračovat v kalkulačce? Y/N: ").strip().lower()
        if wants_continue == "n":
            print("Děkujeme a nashledanou.")
            main()
        elif wants_continue == "y":
            kalkulacka()
        else:
            print("Neplatná volba.")
    
    

def guess_game():

    winning_num = random.randint(1, 30)

    print("Vítejte v hádací hře. Máte 4 pokusy a musíte uhodnout číslo mezi 1 - 30.")
    time.sleep(1)
    print("Hodně štěstí")

    pokus = 0
    pocet_pokusu = 4

    while pokus < pocet_pokusu:
        try:
            guess = int(input("Uhádněte číslo: "))

            if guess < winning_num:
                print(f"Přidej. Toto byl {pokus +1}. pokus")
            elif guess > winning_num:
                print(f"Uber. Toto byl {pokus +1}. pokus")
            else:
                print("Vyhrál jsi :) ")
                break
            pokus += 1
        except ValueError:
            print("Zadejte prosím číslo.")

    if guess != winning_num and pokus == pocet_pokusu:
        print(f"Bohužel jsi nevyhrál. Vítězné číslo bylo {winning_num}")

    while True:
        pokracovat = input("Chcete pokračovat ve hře? Y/N: ").strip().lower()
        if pokracovat == "n":
            print("Děkujeme a nashledanou.")
            main()
        elif pokracovat == "y":
            guess_game()
        else:
            print("Neplatný vstup.")
        
def kanp():

    print("Vítejte ve hře Kámen, Nůžky a Papír\nMyslíš, že mě porazíš? :)")
    time.sleep(1)
    knp = ("kámen", "nůžky", "papír")

    while True:
        player = input("Tak vyber kámen, nůžky nebo papír: ").strip().lower()
        if player not in knp:
            print("Nene, musíš vybrat kámen, nůžky nebo papír")
            continue
        computer = random.choice(knp)

        print(f"Ty jsi vybral {player} a počítač vybral {computer}")
        break

    time.sleep(1)

    while True:
        if (player == "kámen" and computer == "nůžky") or \
           (player == "nůžky" and computer == "papír") or \
           (player == "papír" and computer == "kámen"):
            print("Vyhrál jsi :)")
                
        elif player == computer:
            print("Je to remíza(krab)")
        else:
            print("Prohrál jsi :()")
        break

    while True:
        pokracovat = input("Chcete pokračovat ve hře? Y/N: ").strip().lower()
        if pokracovat == "n":
            print("Děkujeme a hezký den :)")
            main()
        elif pokracovat == "y":
            kanp()
        else:
            print("Chyba, zadej Y nebo N")

def geograpthygame():

    question = {
        "Jaké je hlavní město České republiky: ": "praha",
        "Kolik je na na planetě světadílů?: ": "7",
        "Kolik je na planetš kontinentů: ": "5",
        "Jaký je největší stát USA?: ": "aljaška",
        "V jakém pohoří leží Mt.Everest?: ": "himaláje",
        "V jakém státě leží nejjižnejší cíp Evropy?: ": "španělsko",
        "Jaké je hlavní město Španělska? ": "madrid",
        "Je v Německu nejvíce obyvatel z EU? - ano nebo ne": "ano",
        "Je Francie největší zemí EU? - ano nebo ne": "ano",
        }
    
    list_question = list(question.keys())
    pocet_otazek = 5
    pokus = 0

    all_question = random.sample(list_question, pocet_otazek)

    for idx, i in enumerate(all_question):
        print(f"{idx +1}, {i}")

        odpoved = input("Vaše odpověď?: ").lower()
        spravna_odpoved = question[i]

        if odpoved == spravna_odpoved:
            print("Správně")
            pokus += 1

        else:
            print(f"Špatně, správná odpověď byla {spravna_odpoved.capitalize()}")
    print(f"Konec hry. Tvůj vysledek je {pokus}. z 5ti")


    while True:
        pokracovat = input("Chcete pokračovat ve hře? Y/N: ").strip().lower()
        if pokracovat == "n":
            print("Děkujeme a hezký den :)")
            main()
        elif pokracovat == "y":
            geograpthygame()
        else:
            print("Chyba, zadej Y nebo N")



        
login() 
time.sleep(1)       
def main():

    while True:
        print("=" * 20)
        print("Menu programů")
        print("""
1. Kalkulačka
2. Hádací hra
3. Kámen, Nůžky, Papír
4. Kvíz
5. Konec                              
        """)
        print("=" * 20)

        try:
            user_choice = int(input("Vyberte prosím číselnou možnost z menu: "))
            if user_choice == 1:
                kalkulacka()
            elif user_choice == 2:
                guess_game()
            elif user_choice == 3:
                kanp()
            elif user_choice == 4:
                geograpthygame()    
            elif user_choice == 5:
                print("Děkujeme a hezký den")
                exit()
            else:
                print("Zadejte prosím číselnou možnost z menu")
        except ValueError:
            print("Zadejte prosím možnost z menu")

main()
    