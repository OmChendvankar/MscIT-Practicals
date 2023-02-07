
# PRACTICAL 3 - Utilities and Auditing
# 3B. BINNING
# Om V Chendvankar - 23-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.image as img 
import scipy.stats as stats

np.random.seed(0)

mu = 90 # mean of distribution
sigma = 25 # standard deviation of distribution
x = mu + sigma * np.random.randn(5000)
num_bins = 25

print(x.shape)

fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=1)
# add a 'best fit' line
y = stats.norm.pdf(bins, mu, sigma)
ax.plot(bins, y, '--')
ax.set_xlabel('Example Data')
ax.set_ylabel('Probability density')

sTitle='Histogram ' + str(len(x)) + ' entries into ' + str(num_bins) + ' Bins: $\mu=' + str(mu) + '$, $\sigma=' + str(sigma) + '$'
ax.set_title(sTitle)

fig.tight_layout()

sfilename = 'D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\3 UTILITIES AND AUDITING\\fileplot.png'

fig.savefig(sfilename)

# reading the image 
testImage = img.imread(sfilename) 
plt.imshow(testImage)

