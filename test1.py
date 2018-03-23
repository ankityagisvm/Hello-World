a=1
s=0
print('Please enter a number to add in sum: ')
print('Enter 0 to exit from here:')
while a!=0:
    print('Current sum: ',s)
    a = float(input("Number? "))
    a = float(a)
    s += a
print('Total sum is: ',s)
