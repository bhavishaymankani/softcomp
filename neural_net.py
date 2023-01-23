n = int(input("Enter the number of input neurons: "))
# w will take weight & x will take the input
w = [ ]
x = [ ]

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

y = 0.0
for i in range(0,n):
    y = y + (w[i]*x[i])

print("The net input is ")
print (round(y,3))
