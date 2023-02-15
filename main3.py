#0
print("Tanulok feldolgozása.")

#1
tanulok = []
while True:
    print("\nKérem a tanuló adatait:")
    tanulo={}
    tanulo["nev"] = input("Tanuló neve: ")
    tanulo["szId"] = input("Születési ideje: ")
    tanulo["magassag"] = int(input("Magasság: "))

    tanulok.append(tanulo)

    valasz = input("További tanuli (igen/nem): ")
    if valasz.lower() != 'igen':
        break

#2


#3 Hozzáférés 
print("\nTanulók listája\n")
for item in tanulok:
    #!!!!!Fiygelni kell arra hogy az f-string és a kulcsoknak a határolói különbözőek legyenel!
    print(f'Név: {item["nev"]}, születési ideje: {item["szId"]}, magasság: {item["magassag"]}')