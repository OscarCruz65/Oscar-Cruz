#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=1
suma=0
lista=[]
n5=1
n6=1
while n<2:
    n3=int(input('dame un valor'))
    lista.append(n3)
    suma=suma+n3
    cantidad=len(lista)
    lista.sort()
    print(lista)
    n4=int(input('Calculas porcentaje? 1=si, cualquier otro numero no'))
    if n4==1:
        porcentaje=int(input('porcentaje:'))
        porcentaje2=porcentaje/100
        trimmed=porcentaje2*cantidad
        nfloat=int(trimmed)
        
        if trimmed%2==0:
            print(trimmed)
            trimmed=trimmed/2
            print(lista)
            while n5<=trimmed:
                suma=suma-lista[0]
                lista.pop(0)
                suma=suma-lista[-1]
                lista.pop(-1)
                n5=n5+1
        elif trimmed%2!=0:
            trimmed=trimmed-1
            print(trimmed)
            trimmed=trimmed/2
            print(lista)
            while n5<=trimmed:
                suma=suma-lista[0]
                lista.pop(0)
                suma=suma-lista[-1]
                lista.pop(-1)
                n5=n5+1
        elif trimmed!=nfloat:
            nfloat=nfloat+0.5
            if trimmed<=nfloat:
                trimmed=int(trimmed)
                print(trimmed)
                trimmed=trimmed/2
                print(lista)
                while n5<=trimmed:
                    suma=suma-lista[0]
                    lista.pop(0)
                    suma=suma-lista[-1]
                    lista.pop(-1)
                    n5=n5+1
            elif trimmed>nfloat:
                trimmed=trimmed+1
                trimmed=int(trimmed)
                print(trimmed)
                trimmed=trimmed/2
                print(lista)
                while n5<=trimmed:
                    suma=suma-lista[0]
                    lista.pop(0)
                    suma=suma-lista[-1]
                    lista.pop(-1)
                    n5=n5+1
                
                
        print(lista)
        resultado=suma/len(lista)
        print(f'x{porcentaje}%=:{resultado}')


# In[ ]:




