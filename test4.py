from scipy.stats import ttest_ind
import numpy as np

lause1 = "Arno roomas vargsi mööda klassitoa seinaäärt suure kapi juurde, kus õpetaja Laur maakaarte ja muid koolitarbeid hoidis ning puges kapi alla peitu."
lause2 = "Mu isamaa mu õnn ja rõõm, kui kaunis oled sa"

the = "aeiouõäöü"

def taishaalikute_arv(sona):
    return len([t for t in sona.lower() if t in the])

sonad1 = lause1.split()
sonad2 = lause2.split()

taish1 = [taishaalikute_arv(s) for s in sonad1]
taish2 = [taishaalikute_arv(s) for s in sonad2]

# pisteline kontroll
print("Kontroll:", sonad1[3], taish1[3])
print("Kontroll:", sonad2[2], taish2[2])

# keskmised
print("Lause1 keskmine:", np.mean(taish1))
print("Lause2 keskmine:", np.mean(taish2))

#täishäälikute osakaal
def taishaalikute_osakaal(sona):
    sona = sona.lower()
    taish = len([t for t in sona if t in the])
    kokku = len([t for t in sona if t.isalpha()])
    return taish / kokku if kokku > 0 else 0

osakaal1 = [taishaalikute_osakaal(s) for s in sonad1]
osakaal2 = [taishaalikute_osakaal(s) for s in sonad2]

print("Näide:", sonad1[3], "→ osakaal:", osakaal1[3])
print("Näide:", sonad2[2], "→ osakaal:", osakaal2[2])

import numpy as np

print("Lause1 keskmine täishäälikute osakaal:", np.mean(osakaal1))
print("Lause2 keskmine täishäälikute osakaal:", np.mean(osakaal2))

#Võrrelge t-testiga kahe teksti sõnade täishäälikute osakaale