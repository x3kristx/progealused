#Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
#Väljasta listi esimene väärtus
#Lisa listi lõppu uus puuvili
#Väljasta listi viimane väärtus
#Muuda ühe elemendi väärtust ja väljasta kogu list
#Kontrolli kas väärtus (näiteks õun) eksisteerib listis
#Väljasta listi pikkus
#Eemalda listist element ja väljasta kogu list
#Muuda listi järjekord vastupidiseks
#Sorteeri list ja väljasta
list = ["õun" , "pirn" , "kirss"]
list[2] = "banaan"
a = "pirn"
if a in list:
    print("Pirn on olemas.")
else:
    print("ei ole olemas")
list.sort()
print(list)