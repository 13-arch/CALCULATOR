def addition(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
vir=input('введите выражение: ')
if "+" in vir:
    vir= vir.split('+')
    for i in range(0,len(vir)):
        vir[i]=float(vir[i])
    result=addition(vir[0],vir[i])
    print(result)
if "-" in vir:
    vir= vir.split('-')
    for i in range(0,len(vir)):
        vir[i]=float(vir[i])
    result=subtract(vir[0],vir[i])
    print(result)
if "*" in vir:
    vir= vir.split('*')
    for i in range(0,len(vir)):
        vir[i]=float(vir[i])
    result=multiply(vir[0],vir[i])
    print(result)
if "/" in vir:
    vir= vir.split('/')
    for i in range(0,len(vir)):
        vir[i]=float(vir[i])
    result=divide(vir[0],vir[i])
    print(result)