def maschinengenauigkeit():
    eps = 1.0
    while 1.0 + eps != 1.0:
        eps /= 2.0
    return eps * 2.0

eps = maschinengenauigkeit() 
print(f"Die Maschinengenauigkeit ist: {eps}")



def kleinste_maschinenzahl():
    qmin = 1.0
    while 1.0 + qmin != qmin:
        qmin *=2
    return qmin
qmin = kleinste_maschinenzahl()
print(f"Die kleinste positive Maschinenzahl ist: {qmin}")

