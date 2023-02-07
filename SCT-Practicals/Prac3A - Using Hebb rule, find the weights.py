#Aim: Using Hebb rule, find the weights required to perform the above
# classifications of the given input patterns. The patterns show 3x3 matrix
# form in the square. The '+' symbol represents the value "+1" and the empty
# square represents "-1". Consider "I" belongs to the member of the class (so
# has target value 1) and "O" does not belong to the members of the class
#(so has target value -1)

import numpy as np
#first pattern
x1=np.array([1,1,1,-1,1,-1,1,1,1])
#second pattern
x2=np.array([1,1,1,1,-1,1,1,1,1])
#initialize bais value
b=0
#define target
y=np.array([1,-1])
wtold=np.zeros((9,))
wtnew=np.zeros((9,))
wtnew=wtnew.astype(int)
wtold=wtold.astype(int)
bais=0

print("First input with target =1")
for i in range(0,9):
    wtold[i]=wtold[i]+x1[i]*y[0]
wtnew=wtold
b=b+y[0]

print("Second input with target =-1")
for i in range(0,9):
    wtnew[i]=wtold[i]+x2[i]*y[1]
b=b+y[1]
print("new wt =", wtnew)
print("Bias value",b)
