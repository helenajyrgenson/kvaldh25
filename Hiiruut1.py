#Hii-ruut test 
#Alustuseks võrdlus kahe rühma ja kahe tunnusega 
from scipy import stats 
#Mõlemas tekstis 30 vähemalt viietähelist sõna ning 70 alla viie tähega sõna 
print(stats.chi2_contingency([[30, 70], [30, 70]])[1]) 
#google colab 16.02, hii-ruut