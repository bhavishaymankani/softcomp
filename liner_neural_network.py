import numpy as np

x = float(input("Enter value of x: "))
w = float(input("Enter value w:"))
b = float(input("Enter value b:"))

net = int(w*x+b)

if (net > 1):
    out = 1
elif (net < 0):
    out = 0
elif (net >= 0 & net <=1):
    out = net

print("net",net)
print("out",out)
