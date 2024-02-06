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


def factors(number):
    factorslist = []
    for i in range(1,number+1):
        