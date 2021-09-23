import time 
import math

a=0
b=0
c=0
d=0
x1=0
x2=0


def equation():
    a = int(input("Введите коэфициент a:"))
    b = int(input("Введите коэфициент b:"))
    c = int(input("Введите число c:"))
    print(a)
    d = b**2 - 4*a*c
    x1 = (-b + math.sqrt(d))/(a*2)
    x2 = (-b - math.sqrt(d))/(a*2)
    return " D = {0} \n x1 = {1} \n x2 = {2} \n".format(d,x1,x2)
    

def demult():
    equation()
    return "{0}(x{1}{2})(x{3}{4})".format(a,"+"*norm_to_bool(x1),x1,"+"*norm_to_bool(x2),x2)


def norm_to_bool(nmb):
    return 1-int(nmb <= 0)

act = {
    "1": equation,
    "2": demult
    }

print(act[input(" 1 - решить квадратное уравнение, \n 2 - разложить на множители, \n Что вы хотите сделать? \n >")]())
