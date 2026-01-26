import random
def returning():
    a=random.random()*15
    a=int(a)
    a=chr(a).encode()
    
    return a
x=31
y=10
outs="level.dat"
print( "\n\033c\033[40;37m\ngive the x value of the table ? ")
#x=input()
print( "\n\033[40;37m\ngive the y value of the table ? ")
#y=input()

f1=open(outs,"wb")
for yy in range(y):
    
    for xx in range(x):
        f1.write(returning())
    f1.write(chr(32).encode())
f1.close()