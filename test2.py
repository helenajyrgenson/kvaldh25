from scipy.stats import ttest_ind
import string

lause1 = "Kui arno isaga koolimajja jõudis olid tunnid juba alanud"
lause2 = "Mu isamaa mu õnn ja rõõm, kui kaunis oled sa"

def sonapikkused(lause: str):
    sonad = lause.split()
    # eemaldame kirjavahemärgid sõnade lõpust/algusest (nt "rõõm," -> "rõõm")
    sonad = [s.strip(string.punctuation) for s in sonad]
    return [len(s) for s in sonad]

pikkused1 = sonapikkused(lause1)
pikkused2 = sonapikkused(lause2)

print("Lause1 sõnapikkused:", pikkused1)
print("Lause2 sõnapikkused:", pikkused2)

tulemus = ttest_ind(pikkused1, pikkused2, equal_var=False)  # Welch t-test
print("T-test tulemus:", tulemus)

print("Keskmine lause1:", sum(pikkused1)/len(pikkused1))
print("Keskmine lause2:", sum(pikkused2)/len(pikkused2))
