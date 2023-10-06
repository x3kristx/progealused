#Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). (loogikatehted - logic operators)

nr1 = input("Sisesta esimene number: ")
nr2 = input("Sisesta teine number: ")
nr3 = input("Sisesta kolmas number: ")

if nr1 > nr2 and nr1 > nr3:
    print("Maksimum on:", nr1)
    
elif nr2 > nr1: 
    print("Maksimum on: ", nr2)
else: print("Maksimum on: ", nr3)