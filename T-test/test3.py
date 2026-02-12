#Lisage hümnile ja Kevadele kummalegi ka järgmine lause. Võrrelge p-väärtusi ühe ja kahe lause puhul

from scipy.stats import ttest_ind

lause3 = "Arno roomas vargsi mööda klassitoa seinaäärt suure kapi juurde, kus õpetaja Laur maakaarte ja muid koolitarbeid hoidis ning puges kapi alla peitu."
lause4 = "Kui kaunis oled sa"

def sonapikkused(text):
    return [len(w) for w in text.split()]

tekst_kevad_1 = lause3
tekst_hymn_1 = lause4

a1 = sonapikkused(tekst_kevad_1)
b1 = sonapikkused(tekst_hymn_1)

res1 = ttest_ind(a1, b1)
print("ühe lause p-value on:", res1.pvalue)

#git add . 
#git push



