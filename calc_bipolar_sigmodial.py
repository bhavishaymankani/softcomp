import math

bias = float(input("Enter the value of bias: "))

n = int(input("Enter the number of input neurons: "))

w = [ ]

x = [ ]

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

# Applying Binary Sigmoidal function on the net input i.e  y

binary = 1/(1+ (math.exp(-y)))

print("The output after applying binary sigmoidal function activation ")

print (round(binary, 3))

# Applying Bipolar Sigmoidal function on the net input i.e  y

bipolar = -1+(2/(1+ (math.exp(-y))))

print("The output after applying bipolar sigmoidal function activation ")

print(round(bipolar, 3))
