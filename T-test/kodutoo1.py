from scipy.stats import ttest_ind
import numpy as np
import string

taishaalikud = "aeiouõäöü"

def puhasta_ja_jaga_sonadeks(tekst):
    sonad = tekst.split()
    sonad = [s.strip(string.punctuation) for s in sonad]
    sonad = [s for s in sonad if s != ""]
    return sonad

def taishaalikute_arv(sona):
    sona = sona.lower()
    return len([t for t in sona if t in taishaalikud])

def taishaalikute_osakaal(sona):
    sona = sona.lower()

    # mitu täishäälikut on sõnas
    taish = len([t for t in sona if t in taishaalikud])

    kokku = 0
    for t in sona:
        # arvestame ainult tähti (ilma apostroofide, komade ning punktideta)
        if t in "abcdefghijklmnopqrstuvwxyzõäöü":
            kokku = kokku + 1

    if kokku == 0:
        return 0

    return taish / kokku

# Tekstid, kaks laulu, üks vanem, üks uuem

kungla_rahvas = """
Kui Kungla rahvas kuldsel a’al
kord istus maha sööma,
siis Vanemuine murumaal
läks kandlelugu lööma.

:,:Läks aga metsa mängima,
läks aga laande lauluga.:,:
Läks lauluga, läks lauluga,
läks lauluga!

Säält saivad lind ja lehepuu
ja loomad laululugu,
siis laulis mets ja meresuu
ja eesti rahva sugu.

Läks aga metsa mängima …

Siis kõlas kaunilt lauluviis
ja pärjad pandi pähe.
Ja murueide tütreid siis
sai eesti rahvas näha.

Läks aga metsa mängima …

Ma mängin mättal, mäe peal
ja õhtul hilja õues
ja Vanemuise kandlehääl
see põksub minu põues.

Läks aga metsa mängima …
"""

mina_ja_meri = """
Vaatame kaugusest üksteise poole, mina ja meri, taevas ja maa.
Ootame kohtumist maailma äärel, mina ja meri, taevas ja maa.
Igatsus leegina hingeleel põleb mina ja meri, taevas ja maa.
Kui puutume kokku, kas sulame üheks, mina ja meri, sina ja taevas ja maa.

Suundume ootuses üksteise poole, mina ja meri, taevas ja maa.
Jätame kõrvale kõik argimured, mina ja meri, taevas ja maa.
Unenäo varjudest päriseks saame, mina ja meri, taevas ja maa.
Kui puutume kokku, siis sulame üheks, mina ja meri, sina ja taevas ja maa.

On aega ehk vaadata üksteise poole, mina ja meri, taevas ja maa.
Tormidest väsind kuid soojemast soojem, mina ja meri, taevas ja maa.
Kui õied end keerame valguse poole, mina ja meri, taevas ja maa.
Oma südamelaulu annan su hoolde, mina ja meri, sina ja taevas ja maa.

Lenneldes nii ainult üksteise poole, mina ja meri, taevas ja maa.
Vabana tunda end laotuses suures, mina ja meri, taevas ja maa.
Silmapiir peitub kesk udude loore, mina ja meri, taevas ja maa.
Vaatame ainiti üksteise poole, (mina ja meri) Nagu taevas ja maa

Mere silmad on selged kui maailmapeegel, mina ja meri, taevas ja maa.
Millel loojuva päikese pisaraid veerleb, mina ja meri, taevas ja maa.
Eha loob lõpu päeva veeremisloole, mina ja meri, taevas ja maa.
Nüüd vaatame ainiti üksteise poole, mina ja sina, nagu taevas ja maa.
"""

kungla_sonad = puhasta_ja_jaga_sonadeks(kungla_rahvas)
meri_sonad = puhasta_ja_jaga_sonadeks(mina_ja_meri)

kungla_taish_arvud = [taishaalikute_arv(s) for s in kungla_sonad]
meri_taish_arvud   = [taishaalikute_arv(s) for s in meri_sonad]

kungla_osakaalud = [taishaalikute_osakaal(s) for s in kungla_sonad]
meri_osakaalud   = [taishaalikute_osakaal(s) for s in meri_sonad]

print("PISTELINE KONTROLL (täishäälikute arv):")
print("Kungla rahvas:", kungla_sonad[3], "->", kungla_taish_arvud[3])
print("Mina ja meri:", meri_sonad[3], "->", meri_taish_arvud[3])

print("\nPISTELINE KONTROLL (täishäälikute osakaal):")
print("Kungla rahvas:", kungla_sonad[3], "->", kungla_osakaalud[3])
print("Mina ja meri:", meri_sonad[3], "->", meri_osakaalud[3])

# Keskmised

print("\nSÕNADE ARV (N):")
print("Kungla rahvas N =", len(kungla_sonad))
print("Mina ja meri   N =", len(meri_sonad))

print("\nKESKMISED:")
print("Kungla – keskmine täishäälikute arv sõnas:", np.mean(kungla_taish_arvud))
print("Meri   – keskmine täishäälikute arv sõnas:", np.mean(meri_taish_arvud))

print("Kungla – keskmine täishäälikute osakaal:", np.mean(kungla_osakaalud))
print("Meri   – keskmine täishäälikute osakaal:", np.mean(meri_osakaalud))

# T-test ja p-väärtus

tulemus_arv = ttest_ind(kungla_taish_arvud, meri_taish_arvud, equal_var=False)
tulemus_osakaal = ttest_ind(kungla_osakaalud, meri_osakaalud, equal_var=False)

print("\nT-TEST (täishäälikute arv):")
print("t =", tulemus_arv.statistic)
print("p =", tulemus_arv.pvalue)

print("\nT-TEST (täishäälikute osakaal):")
print("t =", tulemus_osakaal.statistic)
print("p =", tulemus_osakaal.pvalue)
