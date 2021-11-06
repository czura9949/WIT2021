droga = 250
czas = 2.75
predkosc = int(input("Podaj swoją średnią prędkość na trasie: "))
t = droga / predkosc
if t < czas:
    print("Dojedziesz szybciej od pociągu")
else:
    print("Pociąg będzie szybszy")
