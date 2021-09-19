v=[4000,4500,5000,5500,6000,6500,7000]
print('venitul saptamanal a intr. =', sum(v))
print('media venitului zilnic =', sum(v)/7)
if v.index(max(v))==0:
    print('ziua in care sa obtinut cel mai mare venit e luni')
elif v.index(max(v))==1:
    print('ziua in care sa obtinut cel mai mare venit e marti')
elif v.index(max(v))==2:
    print('ziua in care sa obtinut cel mai mare venit e miercuri')
elif v.index(max(v))==3:
    print('ziua in care sa obtinut cel mai mare venit e joi')
elif v.index(max(v))==4:
    print('ziua in care sa obtinut cel mai mare venit e vineri')
elif v.index(max(v))==5:
    print('ziua in care sa obtinut cel mai mare venit e sambata')
else:
    print('ziua in care sa obtinut cel mai mare venit e duminica')
if v.index(min(v))==0:
    print('a)ziua c venitul cel mai mic e luni')
elif v.index(min(v))==1:
    print('a)ziua c venitul cel mai mic e marti')
elif v.index(min(v))==2:
    print('a)ziua c venitul cel mai mic e miercuri')
elif v.index(min(v))==3:
    print('a)ziua c venitul cel mai mic e joi')
elif v.index(min(v))==4:
    print('a)ziua c venitul cel mai mic e vineri')
elif x.index(min(x))==5:
    print('a)ziua c venitul cel mai mic e samabata')
else:
    print('a)ziua cu venitul cel mai mic e duminica')