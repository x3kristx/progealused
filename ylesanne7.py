# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte.
# (paarisarvu mõiste - odd/even)

nr1 = int (input("Sisesta number: "))

if nr1 % 2 == 1:
    print("arv", nr1," on paaritu arv")
else:
    print("arv", nr1, " on paarisarv")