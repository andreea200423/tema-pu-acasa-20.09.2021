t=[1,5,6,7,10,11,19,20,21,20,24,25,26,27,28,29,28,28,20,10,-1,-4,-5,-6]
print('temp. medie e ', sum(t)/24)
print('maximul temp. e ', max(t), 'iar min. = ', min(t))
for i in t:
    if i==max(t):
        print('ora la care sa inr. temperatura max=', t.index(i)+1)
for i in t:
    if i==min(t):
        print('ora la care sa inr. temperatura min=', t.index(i)+1)
n1=0
for i in t:
    if i<0:
        n1+=1
print('e)numarul de zile in care au fost inr. temperaturi mai jos de 0 grade=', n1)
n2=0
for i in t:
    if i>sum(t)//24:
        n2+=1
print('f)numarul de zile in care au fost inr. temp mai mari de media saptamanala=', n2)