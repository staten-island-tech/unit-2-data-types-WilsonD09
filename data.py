""" Challenge 1 
x = float(input("give me a number"))
if (x%2) == 0:
    print('even')
else:
    print('odd') """

""" Challenge 2
x = int(input('Subtotal'))
Service = input('How was the service?')
if Service == ('bad'):
    print(float(x))
elif Service == ('okay'):
    print(float(x*1.15))
elif Service == ('good'):
    print(float(x*1.2))
elif Service == ('great'):
    print(float(x*1.25)) """

""" Challenge 3
def allfactors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors

number = int(input("Please enter a number: "))
listfactors = allfactors(number)
print(listfactors) """

""" Challenge 4
numX = int(input("Please enter the first number: "))
numY = int(input("Please enter the second number: "))
def gcf(numX,numY):
    if numX > numY:
        x = numY
    else:
        x = numX
    for i in range(1,x):
        if numX%i == 0 and numY%i == 0:
            hcf = i
    return hcf
print(gcf(numX,numY)) """