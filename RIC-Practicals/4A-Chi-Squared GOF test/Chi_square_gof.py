# chi-squared test 
from scipy.stats import chi2_contingency
from scipy.stats import chi2
# contingency table
table = [	[11, 7, 5, 5, 11],
			[30,  4,  3, 10,14]]
print(table)
stat, p, dof, expected = chi2_contingency(table)
print('dof = row - 1 * Col - 1 = 2-1 * 5 - 1 = 1*4 ')
print('dof=%d' % dof)
print('Expected : ',expected)
# interpret test-statistic
prob = 0.95
critical = chi2.ppf(prob, dof)
print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
if abs(stat) >= critical:
	print('Data is Dependent (reject H0)')
else:
	print('Data is Independent (H0 Accepted)')
# interpret p-value
alpha = 1.0 - prob
print('significance=%.3f, p=%.3f' % (alpha, p))
if p >= alpha:
	print('H0 Accepted')
else:
	print('H0 Rejected')

