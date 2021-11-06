kap_poczatkowy = int(input("Podaj kapitał początkowy: "))
miesieczne_wplywy = int(input("Podaj miesięczne wpływy: "))
okres_inwestowania = int(input("Podaj okres inwestowania: "))
wart_inwestycji = int(input("Podaj pożądaną końcową wartość inwestycji: "))

wynik = (kap_poczatkowy + miesieczne_wplywy * okres_inwestowania) * 102 / 100

if wynik > wart_inwestycji:
    print("Wynik jest większy niż pożądana wartość inwestycji")
else:
    print("Wynik jest mniejszy niż pożądana wartość inwestycji")
