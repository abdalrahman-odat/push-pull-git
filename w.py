def even(a):
    c=0
    for i in a : 
        if i % 2 == 0 : 
            c+=i
    return c 

print(even([1,2,3,4,5,6,7,8,9,10]))