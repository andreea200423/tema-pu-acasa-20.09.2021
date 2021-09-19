x=[4,5,78,56,43]
y=x
print('a)suma primelor 3 compoente ale variabelei x e', sum(x[0:3]))
print('b)suma tuturor compoentelor variabelei y e', sum(y))
p=1
for i in range (0, len(x)):
    p=p*x[i]
    i+=1
print('c)produsul tuturor compoentelor variabelei x e', p)
print('d)valoarea absolut[ a componentei a 3 a variabelei y e ', abs(x[2]))
print('e)suma primelor componente a variabelelor x si y e ', x[0]+y[0])
