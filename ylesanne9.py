# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi.
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud.
a = float(input("Sisesta külg A: "))
b = float(input("Sisesta külg B: "))
c = float(input("Sisesta külg C: "))

if a < b + c or b < a + c or c < a + b:
    print("on kolmnurk")
    if 
else:
    print("ei ole kolmnurk")

print(a,b,c)