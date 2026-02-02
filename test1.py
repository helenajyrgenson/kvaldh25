from scipy.stats import ttest_ind
print(ttest_ind((3,5,4), (12,16,14)))
print(ttest_ind((3,5,4,6,5,4), (12,16,14,16,15,14)))
print(ttest_ind((13,15,14), (12,16,14))) 

# pip install scipy
