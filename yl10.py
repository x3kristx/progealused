# Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse, kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, kui vanus on 18, siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida.
name = str(input("Mis on teie nimi? "))
print ("Tere: " + name )
location = str(input("Kust kohast te olete pärit? "))
if location == ("Saaremaa"):
    print ("Tere kaassaarlane!")
else:
    print ("Tere!")
age = int(input("Kui vana te olete? "))
if age > 18:
    print ("Palju õnne! Olete piisavalt vana et juhtida autot!")
else:
    print ("Kahjuks olete liiga noor auto juhtimiseks.")
