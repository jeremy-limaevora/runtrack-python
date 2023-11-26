def calcule (n1,operator,n2):
    if operator=="+":
        return n1 + n2
    elif operator=="-":
        return n1-n2
    elif operator=="*":
        return n1*n2
    elif operator=="/":
        return n1//n2
    elif operator=="%":
        return n1%n2

print (calcule(5,"+",5))
print (calcule(16,"-",8))
print (calcule(10,"*",2))
print (calcule(100,"/",2))
print (calcule(2,"%",1))