from scipy.stats import ttest_ind
print(ttest_ind((3,5,4), (12,16,14)))
print(ttest_ind((3,5,4,6,5,4), (12,16,14,16,15,14)))
print(ttest_ind((13,15,14), (12,16,14))) 

# pip install scipy

# T-test on statistiline meetod, millega võrreldakse kahe rühma aritmeetilisi keskmisi, et hinnata, 
# kas nende vahe on piisavalt suur, et seda ei saaks pidada juhuslikuks.
# T-test toimib hästi juhul, kui võrreldakse kahte eristatavat rühma ja mõõdetav tunnus on arvuline.
# Samas ei pruugi T-test anda usaldusväärseid tulemusi väga väikeste rühmade või sobimatute 
# andmete korral.