import math
import datetime

# Pobieranie danych od użytkownika
imie = input("Podaj swoje imię: ")
rok_urodzenia = int(input("Podaj rok urodzenia (YYYY): "))
miesiac_urodzenia = int(input("Podaj miesiąc urodzenia (MM): "))
dzien_urodzenia = int(input("Podaj dzień urodzenia (DD): "))

# Obliczanie ilości dni życia
data_urodzenia = datetime.date(rok_urodzenia, miesiac_urodzenia, dzien_urodzenia)
data_dzisiaj = datetime.date.today()
dni_zycia = (data_dzisiaj - data_urodzenia).days

# Obliczanie biorytmów
def oblicz_biorytm(period, dni):
    return math.sin((2 * math.pi / period) * dni)

fizyczny = oblicz_biorytm(23, dni_zycia)
emocjonalny = oblicz_biorytm(28, dni_zycia)
intelektualny = oblicz_biorytm(33, dni_zycia)

fizyczny_jutro = oblicz_biorytm(23, dni_zycia + 1)
emocjonalny_jutro = oblicz_biorytm(28, dni_zycia + 1)
intelektualny_jutro = oblicz_biorytm(33, dni_zycia + 1)

# Wyświetlanie wyników
print(f"\nWitaj, {imie}! Dziś jest {data_dzisiaj}, to twój {dni_zycia}. dzień życia.")
print("Twój biorytm:")
print(f"Fizyczny: {fizyczny:.2f}")
print(f"Emocjonalny: {emocjonalny:.2f}")
print(f"Intelektualny: {intelektualny:.2f}")

# Sprawdzanie poziomu biorytmów
def sprawdz_biorytm(nazwa, poziom, poziom_jutro):
    if poziom > 0.5:
        print(f"Twój {nazwa} jest dziś na wysokim poziomie!")
    elif poziom < -0.5:
        print(f"Twój poziom {nazwa} jest niski. Odpocznij!")
        if poziom_jutro > poziom:
            print("Nie martw się. Jutro będzie lepiej!")

sprawdz_biorytm("energii", fizyczny, fizyczny_jutro)
sprawdz_biorytm("nastroju", emocjonalny, emocjonalny_jutro)
sprawdz_biorytm("inteligencji", intelektualny, intelektualny_jutro)
