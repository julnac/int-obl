import math
import datetime

def oblicz_biorytmy(dzien_zycia):
    fizyczny = math.sin((2 * math.pi / 23) * dzien_zycia)
    emocjonalny = math.sin((2 * math.pi / 28) * dzien_zycia)
    intelektualny = math.sin((2 * math.pi / 33) * dzien_zycia)
    return fizyczny, emocjonalny, intelektualny

def main():
    imie = input("Podaj swoje imię: ")
    rok = int(input("Podaj rok urodzenia (YYYY): "))
    miesiac = int(input("Podaj miesiąc urodzenia (MM): "))
    dzien = int(input("Podaj dzień urodzenia (DD): "))
    
    data_urodzenia = datetime.date(rok, miesiac, dzien)
    dzisiaj = datetime.date.today()
    dzien_zycia = (dzisiaj - data_urodzenia).days
    
    fizyczny, emocjonalny, intelektualny = oblicz_biorytmy(dzien_zycia)
    fizyczny_jutro, emocjonalny_jutro, intelektualny_jutro = oblicz_biorytmy(dzien_zycia + 1)
    
    print(f"\nWitaj, {imie}! Dziś jest {dzisiaj}, to twój {dzien_zycia}. dzień życia.")
    print(f"Twój biorytm:")
    print(f"Fizyczny: {fizyczny:.2f}")
    print(f"Emocjonalny: {emocjonalny:.2f}")
    print(f"Intelektualny: {intelektualny:.2f}")
    
    for nazwa, wartosc, wartosc_jutro in [("Fizyczny", fizyczny, fizyczny_jutro),
                                          ("Emocjonalny", emocjonalny, emocjonalny_jutro),
                                          ("Intelektualny", intelektualny, intelektualny_jutro)]:
        if wartosc > 0.5:
            print(f"Gratulacje! Twój {nazwa.lower()} biorytm jest wysoki!")
        elif wartosc < -0.5:
            print(f"Twój {nazwa.lower()} biorytm jest niski. Trzymaj się!")
            if wartosc_jutro > wartosc:
                print("Nie martw się. Jutro będzie lepiej!")
    
if __name__ == "__main__":
    main()
