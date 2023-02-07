# Aim: Calculate the output of neural net where input X = [x1, x2] = [0.2, 0.6] &
# Weight W = [w1, w2] = [0.3,0.7]& bias = 0.45

# bias = 0.45
bias = float(input("Enter the value of bias: "))
# n will take no of neurons in the network.
n = int(input("Enter the number of input neurons: "))
# w will take weight & x will take the input
w = []
x = []

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

print("The net input is ")
print (round(y,3))
