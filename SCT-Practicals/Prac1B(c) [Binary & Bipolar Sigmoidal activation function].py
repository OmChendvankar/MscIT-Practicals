# Aim: Calculate the output of neural net where input X = [x1, x2, x3] = [0.8, 0.6, 0.4]] &
# Weight W = [w1, w2, w3] = [0.1, 0.3, -0.2] & bias =0.35.
# Apply Binary & Bipolar Sigmoidal activation function
# import math so that we can use mathematical function exp()

import math

bias = float(input("Enter the value of bias: "))
# n will take no of neurons in the network.
n = int(input("Enter the number of input neurons: "))
# w will take weight & x will take the input
w = []
x = []

# taking the value of input and their weight
for i in range(0,n):
    a = float(input("Enter the input: "))
    x.append(a)
    b = float(input("Enter the weight: "))
    w.append(b)

print("The given weights are: ")
print(w)
print("The given input are: " )
print(x)

y = bias
for i in range(0,n):
    y = y + (w[i]*x[i])

print("The calculated net input y : ")
print(y)

# Applying Binary Sigmoidal function on the net input i.e y
binary = 1/(1+ (math.exp(-y)))
print("The output after applying binary sigmoidal function activation ")
print (round(binary, 3))

# Applying Bipolar Sigmoidal function on the net input i.e y
bipolar = -1+(2/(1+ (math.exp(-y))))
print("The output after applying bipolar sigmoidal function activation ")
print (round(bipolar, 3))
