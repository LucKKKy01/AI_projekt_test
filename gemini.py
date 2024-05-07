def pobierz_dane():
  """
  Funkcja pobiera od użytkownika liczby i operator matematyczny.
  """
  liczba1 = float(input("Podaj pierwszą liczbę: "))
  operator = input("Podaj operator (+, -, *, /, %): ")
  liczba2 = float(input("Podaj drugą liczbę: "))
  return liczba1, operator, liczba2

def wykonaj_obliczenia(liczba1, operator, liczba2):
  """
  Funkcja wykonuje obliczenia na podstawie podanych liczb i operatora.
  """
  if operator == "+":
    wynik = liczba1 + liczba2
  elif operator == "-":
    wynik = liczba1 - liczba2
  elif operator == "*":
    wynik = liczba1 * liczba2
  elif operator == "/":
    if liczba2 == 0:
      print("Nie można dzielić przez zero!")
      return None
    else:
      wynik = liczba1 / liczba2
  elif operator == "%":
    wynik = liczba1 % liczba2
  else:
    print("Nieznany operator!")
    return None
  return wynik

def wyswietl_wynik(wynik):
  """
  Funkcja wyświetla wynik obliczeń.
  """
  if wynik is not None:
    print(f"Wynik: {wynik}")
  else:
    print("Wystąpił błąd.")

def main():
  """
  Funkcja główna programu.
  """
  while True:
    liczba1, operator, liczba2 = pobierz_dane()
    wynik = wykonaj_obliczenia(liczba1, operator, liczba2)
    wyswietl_wynik(wynik)

    kontynuowac = input("Czy chcesz wykonać kolejne obliczenie? (t/n): ")
    if kontynuowac.lower() != "t":
      break

if __name__ == "__main__":
  main()