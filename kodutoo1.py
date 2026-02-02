from scipy.stats import ttest_ind
import numpy as np

tekst1 = "Õhtul oli linnas tuul ja kohvikus oli soe inimesed rääkisid vaikselt"
tekst2 = "Hommikul oli metsas lumi krudisev ja valgus terav rada oli vaikne"

def sonapikkused(text):
    return [len(w) for w in text.split()]

a = sonapikkused(tekst1)
b = sonapikkused(tekst2)

print("Tekst1 keskmine:", np.mean(a))
print("Tekst2 keskmine:", np.mean(b))

res = ttest_ind(a, b)
print("T-test:", res)

# T-test on statistiline meetod, millega võrreldakse kahe rühma aritmeetilisi keskmisi, et hinnata, 
# kas nende vahe on piisavalt suur, et seda ei saaks pidada juhuslikuks.
# T-test toimib hästi juhul, kui võrreldakse kahte eristatavat rühma ja mõõdetav tunnus on arvuline.
# Samas ei pruugi T-test anda usaldusväärseid tulemusi väga väikeste rühmade või sobimatute 
# andmete korral.