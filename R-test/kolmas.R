# print(prop.test (20, 120))
# proportsioonide test
# print (prop.test(20,120, p=0,2))   .....ei tööta

#mida on mõtet prop testiga mõõta ja mida pole? n: print(prop.test (265, 170)) ei toimi. Kasutad seda
#kus on võimalik midagi mõistlikult lugeda, sellist andmestikku

#Näide
#Norral seitse kuldmedalit ja kuldmedaleid kokku 37. 
print(prop.test (7, 37))
norra=7
kokku=37
vahemik= prop.test (norra, kokku) $conf.int
print(vahemik)
print(vahemik*kokku)

#Näide, erakondade reitingud
print(prop.test(266,1000)) #kakssada kuuskümmendkuus tuhandest ütlesid et valiks isamaa

print(prop.test(139,1000))

print(prop.test(c(147,139), c(1000,1000))) # 147, 139.....jne on toetajad. 1000,1000 on üleüldiselt inimesed. Tulemuseks: midagi on kõrgem, midagi on madalam.
# et saada rohkem tulemusi, vaja oleks rohkem inimesi....
# Näiteks:
print(prop.test(c(1470,1390), c(10000,10000), conf.level=0,95)) #Siin see conf.leveli asi ei tööta???

#Nimede loendi näide. Regex, regular expressions. Google sheets (countif(B1:B586, "=q"))...vst oli q, võis olla ka g. Sõna viimased tähed (midA1586, len(A1586), 1) - google sheets

print(prop.test(644,))


