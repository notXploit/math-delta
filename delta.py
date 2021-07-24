import math
from time import sleep

print('██████╗░███████╗██╗░░░░░████████╗░█████╗░')
print('██╔══██╗██╔════╝██║░░░░░╚══██╔══╝██╔══██╗')
print('██║░░██║█████╗░░██║░░░░░░░░██║░░░███████║')
print('██║░░██║██╔══╝░░██║░░░░░░░░██║░░░██╔══██║')
print('██████╔╝███████╗███████╗░░░██║░░░██║░░██║')
print('╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝')
print('by Yasser Mob')
while True:
    sleep(2)
    print('Enter A B C ')
    try:
       a = int(input('A= '))
       b = int(input('B= '))
       c = int(input('C= '))
       delta = b*b-4*a*c
       sleep(1)
       print('delta is ',delta)
    except:
        sleep(2)
        print('this is not a number, repeat after 2 second !')
        sleep(2)
        continue
    if delta > 0:
        x1 = -b+math.sqrt(delta)/2*a
        x2 = -b-math.sqrt(delta)/2*a
        sleep(2)
        print('x1= ',x1,' x2= ',x2)
    elif delta == 0:
        x1 = -b/2*a
        x2 = x1
        sleep(2)
        print('x1= ',x1,' x2= ',x2)
    elif delta <0:
        sleep(2)
        print('pas de solution delta < 0')
    re = input('repeat or close ? r/c: ')
    if re == 'r':
        print('repeat after 2 second !')
        sleep(2)
        continue
    elif re == 'c':
        print('close after 2 second')
        sleep(2)
        quit()
    else:
        print('wrong command close after 2 second !')
        sleep(2)
        quit()
# By Yasser Mob 
# instagram : real.yassermob   