# *args, **kwargs

def suma(a,b):
    return a+b

print(suma(8,6))

def suma2 (*args): #*args es una tupla de longitud variable
    total = 0
    for i in args:
        total +=i
    return total

print(suma2(4,5,6,8,7))     
print(suma2(1,2,3,5,7))   
print(suma2(5,6,7,8,9,0))

def suma3(**kwargs):
    total=0
    for i in kwargs:
        total += kwargs[i]
    return total

print(suma3(a=1, b=20, c=30))
print(suma3(a=20, b=20, c=30, d=1000))
