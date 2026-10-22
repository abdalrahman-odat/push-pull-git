# ---------------------------- P1

def even(a):
    c=0
    for i in a : 
        if i % 2 == 0 : 
            c+=i
    return c 

print(even([1,2,3,4,5,6,7,8,9,10]))

# ---------------------------- P2

def l(a):
    sl=0
    cl=0
    number=0

    for i in a : 
        if i.isdigit() :
            number+=1
        elif i.isalpha() :
            if i.isupper() :
                cl+=1
            else :
                sl+=1
    return number , cl , sl

s=input("enter : ")
print(l(s))

# ---------------------------- P3
print("fourth")
