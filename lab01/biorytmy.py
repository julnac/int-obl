import math
import datetime

imie = input("Podaj swoje imię: ")
rok = int(input("Podaj rok urodzenia (YYYY): "))
miesiac = int(input("Podaj miesiąc urodzenia (MM): "))
dzien = int(input("Podaj dzień urodzenia (DD): "))

# dni życia
data_urodzenia = datetime.date(rok, miesiac, dzien)
dzisiaj = datetime.date.today()
dzien_zycia = (dzisiaj - data_urodzenia).days

# biorytmy
fizyczny = math.sin((2 * math.pi / 23) * dzien_zycia)
emocjonalny = math.sin((2 * math.pi / 28) * dzien_zycia)
intelektualny = math.sin((2 * math.pi / 33) * dzien_zycia)

#jutro
fizyczny_jutro = math.sin((2 * math.pi / 23) * (dzien_zycia + 1))
emocjonalny_jutro = math.sin((2 * math.pi / 28) * (dzien_zycia + 1))
intelektualny_jutro = math.sin((2 * math.pi / 33) * (dzien_zycia + 1))

print(f"\nWitaj, {imie}! Dziś jest {dzisiaj}, to twój {dzien_zycia}. dzień życia.")
print("Twój biorytm:")
print(f"Fizyczny: {fizyczny:.2f}")
print(f"Emocjonalny: {emocjonalny:.2f}")
print(f"Intelektualny: {intelektualny:.2f}")

if fizyczny > 0.5:
    print("Masz dziś dużo energii! Super!")
elif fizyczny < -0.5:
    print("Twój poziom energii jest niski. Odpocznij!")
    if fizyczny_jutro > fizyczny:
        print("Nie martw się. Jutro będzie lepiej!")

if emocjonalny > 0.5:
    print("Twój nastrój jest dziś świetny!")
elif emocjonalny < -0.5:
    print("Możesz czuć się gorzej emocjonalnie. Dbaj o siebie!")
    if emocjonalny_jutro > emocjonalny:
        print("Nie martw się. Jutro będzie lepiej!")

if intelektualny > 0.5:
    print("Twój umysł jest dziś bardzo bystry!")
elif intelektualny < -0.5:
    print("Dziś może być trudniej skupić się na problemach.")
    if intelektualny_jutro > intelektualny:
        print("Nie martw się. Jutro będzie lepiej!")

#1 godzina
